import pickle
import os

import frontend.input_function
import library_backend
from frontend import *
from frontend import input_function
from library_backend import exception

if __name__ == '__main__':

    library = None
    if os.path.exists('library.pickle'):
        with open('library.pickle', 'rb') as f:
            library = pickle.load(f)
    else:
        print('Hello, this the first time you start library program.')
        library = frontend.input_function.start_library()
    try:
        while True:
            # try:
            print('In any time you wish to leave the program insert: "#"')
            user_choice = input('What would you like to do?\n'
                                'To add a new customer or new book insert "1"\n'
                                'To Loan or return a book insert "2"\n'
                                'To display information of loans, books, or customer insert "3"\n'
                                'To remove a book or customer from library insert "4"\n'
                                'To find a book insert "5"\n'
                                'To find a customer insert "6"\n'
                                'Insert your choice here:\n')
            if user_choice not in ('1', '2', '3', '4', '5', '6', '#'):
                print('your choice is invalid, please try again: \n')
            elif user_choice == "1":
                user_add_choice = input_function.add_choice()
                while True:
                    if user_add_choice == '1':
                        book = input_function.add_a_book()
                        try:
                            library.add_book(book)
                            print('All good, the has enter the library.')
                            user_choice = None
                            break
                        except exception.BookExistsError(book.get_book_id()) as e:
                            print(f'The book ID {e} is already in the system try again: ')
                        except exception.LibraryException as e:
                            print('something went wrong please try again')
                    elif user_add_choice == '2':
                        customer_address = input_function.create_address()
                        customer = input_function.create_customer(customer_address)
                        try:
                            library.add_customer(customer)
                            print('All good, the has enter the library.')
                            user_choice = None
                            break
                        except exception.CustomerExistsError(customer.get_customer_id()) as e:
                            print(f'The customer ID {e} is already in the system try again: ')
                        except exception.LibraryException as e:
                            print('something went wrong please try again')
                    elif user_add_choice == "#":
                        user_choice = None
                        break
            elif user_choice == "2":
                user_loan_choice = input_function.loan_choice()
                if user_loan_choice == '1':
                    customer_id_loan = input_function.customer_id_valid()
                    book_id_loan = input_function.book_id_valid()
                    while True:
                        try:
                            library.loan_book(book_id_loan, customer_id_loan)
                            print('Enjoy your reading, dont forget to return in time.')
                            break
                        except exception.CustomerExistsError(customer_id_loan) as e:
                            print(f'The customer ID {e} is not in the system try again: ')
                        except exception.BookExistsError(book_id_loan) as e:
                            print(f'The book ID number dose not exists, try again: ')
                        except exception.BookAlreadyLoaned(book_id_loan) as e:
                            print('The book is already loaned, you cant loaned it!!! ')
                        except exception.LateReturnPunishment(customer_id_loan) as e:
                            print(f'Dear {library.get_customer_by_id(customer_id_loan).get_customer_first_name()}'
                                  f' you were late to return your latest loaned book therefore you cant loan this'
                                  f' book. You got punished and i got the BONUS!!! ')
                        except exception.LibraryException() as e:
                            print('something went wrong please try again')
                elif user_loan_choice == '2':
                    while True:
                        book_id_return = None
                        try:
                            book_id_return = input_function.book_id_valid()
                            library.return_book(book_id_return)
                            print('book returned!')
                            break
                        except exception.BookExistsError(book_id_return) as e:
                            print(f'Book number{e} is not loaned, so.... you cant return it.')
                        except exception.LateReturnPunishment(book_id_return) as e:
                            print('Customer returned book LATE!!! Unlease the librarian in you and kill him.'
                                  'Just kidding you cant loan another book for thr next two weeks.'
                                  'You got punish and i got the BONUS!!!')
                        except exception.LibraryException() as e:
                            print('something went wrong please try again')
                    if user_loan_choice == "#":
                        break
            elif user_choice == "3":
                user_information_choice = input_function.information_to_display()
                if user_information_choice == '1':
                    print(library.display_all_books())
                elif user_information_choice == '2':
                    print(library.display_all_customer())
                elif user_information_choice == '3':
                    # Display only the books that are currently loaned, just in case there is a function in Library that
                    # display all the loans (returned and late)
                    print(library.get_loaned_book())
                elif user_information_choice == '4':
                    print(library.get_late_returned())
                elif user_information_choice == "5":
                    while True:
                        customer_id_display_loan = input_function.customer_id_valid()
                        try:
                            print(library.display_customer_loans(customer_id_display_loan))
                            break
                        except exception.CustomerExistsError(customer_id=customer_id_display_loan) as e:
                            print(f'The customer ID number {e} dos not exist in our recorde')
                        except exception.LibraryException() as e:
                            print('something went wrong try again: ')
            elif user_choice == "4":
                user_remove_choice = input_function.remove_option()
                if user_remove_choice == "1":
                    while True:
                        book_id_remove = input_function.book_id_valid()
                        try:
                            library.remove_book_from_library(book_id_remove)
                            print('Book removed all is good "YUFI TUFI')
                            break
                        except exception.BookExistsError(book_id_remove) as e:
                            print(f'The book ID number {e} dos not exist in our recorde')
                        except exception.LibraryException() as e:
                            print('something went wrong try again: ')
                elif user_remove_choice == "2":
                    while True:
                        customer_id_remove = input_function.customer_id_valid()
                        try:
                            library.remove_customer(customer_id_remove)
                            print('Customer removed "No more soup for you"')
                            break
                        except exception.CustomerExistsError(customer_id_remove) as e:
                            print(f'The customer ID number {e} dos not exist in our recorde')
                        except exception.CantRemoveCustomer(customer_id_remove) as e:
                            print(f'The customer ID number {e} have a loaned book, he cant be removed.')
                        except exception.LibraryException() as e:
                            print('something went wrong try again: ')
                else:
                    break
            elif user_choice == "5":
                user_find_choice = input_function.find_choice()
                if user_find_choice == "1":
                    book_num_to_find = input('Enter book name: ').lower()
                    while True:
                        if len(library.get_book_by_name(book_num_to_find)) == 0:
                            print('There are no books under that name:')
                        else:
                            print(library.get_book_by_name(book_num_to_find))
                elif user_find_choice == '2':
                    name_to_find = input_function.find_by_first_or_last_name('author')
                    if len(library.get_book_by_author_first_name(name_to_find)) == 0 \
                            and len(library.get_book_by_author_last_name(name_to_find)) == 0:
                        print('There are no books under that author name.')
                    else:
                        print(f'result by first name:\n{library.get_book_by_author_first_name(name_to_find)}\n'
                              f'result by last name: \n{library.get_book_by_author_last_name(name_to_find)}')
                else:
                    break
            elif user_choice == '6':
                customer_to_find = input_function.find_by_first_or_last_name('customer')
                if len(library.get_book_by_author_first_name(customer_to_find)) == 0 \
                        and len(library.get_book_by_author_last_name(customer_to_find)) == 0:
                    print('There are no books under that author name.')
                else:
                    print(f'result by first name:\n{library.get_book_by_author_first_name(customer_to_find)}\n'
                          f'result by last name: \n{library.get_book_by_author_last_name(customer_to_find)}')
            else:
                break
    except exception.LibraryException() as e:
        print("error occurred, saving and exiting")
    finally:
        with open('library.pickle', 'wb') as f:
            pickle.dump(library, f)
