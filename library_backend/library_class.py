from library_backend.book_code import Book
from library_backend.customer_code import Customer
import datetime
from library_backend import exception
from library_backend import address_class
from library_backend.loan_code import Loan


class Library:
    def __init__(self, library_name: str, city: str):
        self._address = city
        self._library_name = library_name
        self._books: dict[str, Book] = {}
        self._costumers: dict[str, Customer] = {}
        self._loans: dict[str, Loan] = {}
        self._returned_loans: dict[str, list[Loan]] = {}
        self._late_returned_loan:  dict[str, list[Loan]] = {}
        self._costumer2loan: dict[str, set[Loan]] = {}

    def get_books(self):
        return self._books

    def get_book_by_name(self, book_name: str) -> list[Book]:
        ret_val = []
        for book_id, book in self._books.items():
            if book.get_book_name() == book_name:
                ret_val.append(book)
        return ret_val

    def get_book_by_author_first_name(self, author_first_name) -> list[Book]:
        ret_val = []
        for book_id, book in self._books.items():
            if book.get_author_first_name() == author_first_name:
                ret_val.append(book)
        return ret_val

    def get_book_by_author_last_name(self, author_last_name) -> list[Book]:
        ret_val = []
        for book_id, book in self._books.items():
            if book.get_author_last_name() == author_last_name:
                ret_val.append(book)
        return ret_val

    def get_customer_dict(self):
        return self._costumers

    def get_customer_by_id(self, customer_id: str) -> Customer:
        if customer_id in self._costumers:
            return self._costumers[customer_id]

    def get_customer_by_first_name(self, customer_first_name) -> list[Customer]:
        ret_val = []
        for customer_id, customer in self._costumers.items():
            if customer.get_customer_first_name() == customer_first_name:
                ret_val.append(customer)
        return ret_val

    def get_customer_by_last_name(self, customer_last_name) -> list[Customer]:
        ret_val = []
        for customer_id, customer in self._costumers.items():
            if customer.get_customer_last_name() == customer_last_name:
                ret_val.append(customer)
        return ret_val

    def get_library_name(self):
        return self._library_name

    def get_address(self):
        return self._address

    def add_customer(self, customer: Customer):
        if customer.get_customer_id() in self._costumers:
            raise exception.CustomerExistsError(customer.get_customer_id())
        else:
            self._costumers[customer.get_customer_id()] = customer
            self._returned_loans[customer.get_customer_id()] = []
            self._late_returned_loan[customer.get_customer_id()] = []
            return True

    def add_book(self, book: Book):
        if book.get_book_id() in self._books:
            raise exception.BookExistsError(book.get_book_id())
        else:
            self._books[book.get_book_id()] = book
            return True

    def loan_book(self, book_id: str, customer_id: str) -> bool:
        if book_id in self._loans:
            raise exception.BookAlreadyLoaned(book_id)
        elif customer_id not in self._costumers:
            raise exception.CustomerExistsError(customer_id)
        elif book_id not in self._books:
            raise exception.BookExistsError(book_id)
        else:
            for loan in self._returned_loans[customer_id]:
                if loan.get_return_date() + datetime.timedelta(weeks=2) > datetime.datetime.now():
                    raise exception.LateReturnPunishment(customer_id)
            book_to_loan = Loan(customer_id, book_id, datetime.datetime.now(), self._books[book_id].get_type_of_loan())
            self._loans[book_id] = book_to_loan
            return True

    def return_book(self, book_id: str):
        return_date = datetime.datetime.now()
        if book_id not in self._loans:
            raise exception.BookExistsError(book_id)
        else:
            transfer_loan = self._loans[book_id]
            self._loans.pop(book_id)
            if transfer_loan.get_max_return_date() > return_date:
                self._returned_loans[transfer_loan.get_customer()].append(transfer_loan)
                return True
            elif transfer_loan.get_max_return_date() < return_date:
                self._late_returned_loan[transfer_loan.get_customer()].append(transfer_loan)
                raise exception.LateReturnPunishment(book_id)

    def display_all_books(self):
        all_book_list = []
        for book in self._books.values():
            all_book_list.append(book)
        return all_book_list

    def display_all_customer(self):
        all_customer_list = []
        for customer in self._costumers.values():
            all_customer_list.append(customer)
        return all_customer_list

    def display_all_loans(self) -> dict:
        all_loans_list = {'loaned': [],
                          'late returned': [],
                          'returned': []}
        for loan in self._loans.values():
            all_loans_list['loaned'].append(loan)
        for returned in self._returned_loans.values():
            all_loans_list['returned'].append(returned)
        for late in self._late_returned_loan.values():
            all_loans_list['late returned'].append(late)
        return all_loans_list

    def get_loaned_book(self):
        return self._loans

    def get_returned_loans(self):
        return self._returned_loans

    def get_late_returned(self):
        return self._returned_loans

    def display_customer_loans(self, customer_id: str):
        if customer_id not in self._costumers:
            raise exception.CustomerExistsError
        else:
            all_customer_loans_list = []
            loans = self._costumer2loan[customer_id]
            for loan in loans:
                all_customer_loans_list.append(loan)
            return all_customer_loans_list

    def remove_book_from_library(self, book_id: str) -> bool:
        if book_id not in self._books:
            raise exception.BookExistsError(book_id)
        else:
            self._books.pop(book_id)
            for book in self._loans:
                if book == book_id:
                    self._loans.pop(book_id)
            for customer in self._returned_loans.values():
                for loan in customer:
                    if loan.get_book_id() == book_id:
                        customer.pop(customer.index(loan))
            for customer in self._late_returned_loan.values():
                for loan in customer:
                    if loan.get_book_id() == book_id:
                        customer.pop(customer.index(loan))
            return True

    def remove_customer(self, customer_id: str) -> bool:
        if customer_id not in self._costumers:
            raise exception.CustomerExistsError(customer_id)
        elif customer_id in self._loans:
            raise exception.CantRemoveCustomer(customer_id)
        else:
            self._costumers.pop(customer_id)
            return True


