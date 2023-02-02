from library_backend.book_code import Book
from library_backend.customer_code import Customer
import datetime

from library_backend.loan_code import Loan


class Library:
    def __init__(self, library_name: str, address: classmethod):
        self._address = address
        self._library_name = library_name
        self._books: dict[str, Book] = {}
        self._costumers: dict[str, Customer] = {}
        self._loans: dict[str, Loan] = {}
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
        else:
            return False

    def get_customer_by_first_name(self, customer_first_name) -> list[Customer]:
        ret_val = []
        for customer_id, customer in self._costumers.items():
            if customer.get_customer_first_name() == customer_first_name:
                ret_val.append(customer)
        return ret_val

    def get_customer_by_last_name(self, customer_last_name) -> list[Customer]:
        ret_val = []
        for customer_id, customer in self._costumers.items():
            if customer.get_customer_first_name() == customer_last_name:
                ret_val.append(customer)
        return ret_val

    def get_library_name(self):
        return self._library_name

    def get_address(self):
        return self._address

    def add_customer(self, customer_id: str, customer_name: dict, address: classmethod, email: str, birth_day: datetime):
        if customer_id in self._costumers:
            return False
        else:
            customer = Customer(customer_id, customer_name, address, email, birth_day)
            self._costumers[customer_id] = customer
            return True

    def add_book(self, book_id: str, book_name: str, author: dict, year_publish: str, type_of_loan: int):
        if book_id in self._books:
            return False
        else:
            book = Book(book_id, book_name, author, year_publish, type_of_loan)
            self._books[book_id] = book
            return True

    def loan_book(self, book_id: str, customer_id: str) -> bool:
        if book_id in self._loans:
            return False
        if customer_id not in self._costumers:
            return False
        else:
            book_to_loan = Loan(customer_id, book_id, datetime.datetime.now(), self._books[book_id].get_type_of_loan())
            self._loans[book_id] = book_to_loan
            return True

    def return_book(self, book_id: str) -> bool:
        if book_id in self._loans:
            self._books.pop(book_id)
            return True
        else:
            return False

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

    def display_all_loans(self):
        all_loans_list = []
        for loan in self._loans:
            all_loans_list.append(loan)
        return all_loans_list

    def display_customer_loans(self, customer_id: str):
        if customer_id in self._costumers:
            all_costomer_loans_list = []
            loans = self._costumer2loan[customer_id]
            for loan in loans:
                all_costomer_loans_list.append(loan)
            return all_costomer_loans_list
        else:
            return False

    def remove_book_from_library(self, book_id: str) -> bool:
        if book_id not in self._books:
            self._books.pop(book_id)
            return True
        else:
            return False

    def remove_customer(self, customer_id: str) -> bool:
        if customer_id in self._costumers and customer_id not in self._loans:
            self._costumers.pop(customer_id)
            return True
        else:
            return False


# if __name__ == '__main__':
#     jfh = Book('123456', 'noam', {'dfg': 'dfg'}, '1983', 3)
#
#     print(Library.time_loan_2_max_days('123456', '123456'))
