import datetime
from frontend import input_function
from library_backend import library_class
from library_backend import exception

if __name__ == '__main__':
    library: library_class.Library = None
    print('hello there, before we start')
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
            elif user_choice == 1:
                user_add_choice = None
                while user_add_choice not in (1, 2, '#'):
                    user_add_choice = input('What would you lik to add:\n'
                                            'To add a book insert 1\n'
                                            'To add a customer insert 2:\n'
                                            '')
                    if user_add_choice == 1:
                        while True:
                            try:
                                book = input_function.add_a_book()
                                library.add_book(book)
                                print('All good, the has enter the library.')
                                break
                            except exception.BookExistsError(book.get_book_id()) as e:
                                print(f'The book ID {e} is already in the system try again: ')
                            except exception.LibraryException as e:
                                print('something went wrong please try again')
                    elif user_add_choice == 2:
                        while True:
                            try:
                                customer_address = input_function.create_address()
                                customer = input_function.create_customer(customer_address)
                                library.add_customer(customer)
                                print('All good, the has enter the library.')
                                break
                            except exception.CustomerExistsError(customer.get_customer_id()) as e:
                                print(f'The customer ID {e} is already in the system try again: ')
                            except exception.LibraryException as e:
                                print('something went wrong please try again')














