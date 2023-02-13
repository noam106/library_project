import library_backend.customer_code
import library_test.useful_function
from library_test import useful_function
from library_backend import library_class, address_class
from library_backend import loan_code


def create_address() -> address_class.Address :
    while True:
        customer_address_city = input('Insert customer city address: ')
        customer_address_street = input('Insert customer street address: ')
        customer_house_num = input('Insert customer house number: ')
        customer_zipcode = input('Insert customer zipcode: ')

        if useful_function.is_digit(customer_zipcode) is False or useful_function.is_digit(customer_house_num)\
                is False or useful_function.is_str_valid(customer_address_street) is False or\
                useful_function.is_str_valid(customer_address_city) is False:
            print('one of your inputs is not valid, please try again: ')
        else:
            break

    customer_address = address_class.Address(customer_address_street, customer_address_city,
                                             customer_zipcode, customer_house_num)
    print('address created')
    return customer_address


def create_customer(customer_address) -> library_backend.customer_code.Customer:
    while True:
        customer_last_name = input('Insert customer last name: ').lower()
        customer_first_name = input('Insert customer first name: ').lower()
        customer_id = input('Insert customer id number: ')
        customer_email = input('Insert customer email: ').lower()
        customer_bday = input('Insert customer birth day in the falling order DD/MM/YYYY: ')
        customer_full_name = customer_first_name + " " + customer_last_name
        if useful_function.is_valid_name(customer_full_name) is False:
            print('There is something wrong with the customer name please try again: ')
        elif useful_function.is_digit(customer_id) is False:
            print('There is something wrong with the customer ID number please try again: ')
        elif useful_function.isvalid_email(customer_email) is False:
            print('There is something wrong with the customer e-mail please try again: ')
        elif useful_function.is_valid_bday(customer_bday) is False:
            print('There is something wrong with the customer birth day please try again: ')
        else:
            customer_name_dict = {'first_name': customer_first_name,
                                  'last_name': customer_last_name}
            break
    customer = library_backend.customer_code.Customer(customer_id, customer_name_dict, customer_address,
                                                      customer_email, customer_bday)
    print('All good')
    return customer


def add_a_book() -> library_backend.library_class.Book:
    while True:
        book_id = input('Insert the book ID: ')
        book_name = input('Insert the book name: ').lower()
        author_last_name = input('Insert author last name: ').lower()
        author_first_name = input('Insert author first name: ').lower()
        year_publish = input('Insert the year of book publish: ')
        book_type = input('Insert the book type, "1", "2" or "3": ')
        author_full_name = author_first_name + " " + author_last_name
        if useful_function.is_digit(book_id) is False:
            print('There is something wrong with the book ID number please try again')
        elif useful_function.is_valid_name(author_full_name) is False:
            print('There is something wrong with the author name please try again: ')
        elif useful_function.is_digit(year_publish) is False:
            print('There is something wrong with the year of book publish, try again: ')
        elif book_type not in ("1", "2", "3"):
            print('Book type can be only "1", "2", or "3". Please try again: ')
        else:
            author_name_dict = {'first_name': author_first_name,
                                'last_name': author_last_name}
            book = library_backend.library_class.Book(book_id, book_name,
                                                      author_name_dict, year_publish, book_type)
            print('all good, checking if the book in the system...')
            break
    return book


def information_to_display() -> str:
    print('Witch information you wish to display: ')
    choice_tuple = ("1", "2", "3", "4", "5", "#")
    user_choice = None
    while True:
        user_choice = input('To display all book insert "1": \n'
                            'To display all customers insert "2": \n'
                            'To display all loans insert "3": \n'
                            'To display all late loans insert "4": \n'
                            'To display all the loans fo a specific customer insert "5": \n'
                            'Insert your choice here: ')
        if user_choice not in choice_tuple:
            print('Your choice need to be one of the following: "1", "2", "3", "4", "5". Try again.')
        else:
            break
    return user_choice


def customer_id_valid() -> str:
    customer_id = input('Enter customer ID number:  ')
    while True:
        if useful_function.is_digit(customer_id) is False:
            print('There is something wrong with the customer ID number please try again: ')
        else:
            break
    return customer_id


def remove_option() -> str:
    customer_choice = None
    while True:
        customer_choice = input('If you wish to remove a book from library insert 1: \n'
                                'If you wish to remove a customer from library insert 2: \n'
                                'Enter your choice: ')
        if customer_choice not in ('1', '2', '#'):
            print('Your choice need to be one of the following: "1" or "2". Try again.')
        else:
            break
    return customer_choice


def book_id_valid() -> str:
    book_id = None
    while True:
        book_id = input("Insert the book ID: ")
        if useful_function.is_digit(book_id) is False:
            print('There is something wrong with the book ID number please try again: ')
        else:
            break
    return book_id


def loan_choice() -> str:
    user_loan_choice = None
    while True:
        user_loan_choice = input('To loan a book insert 1: \n'
                                 'To return a book insert 2: ')
        if user_loan_choice not in ("1", "2", '#'):
            print('Your can only choose between 1 or 2. Try again ')
        else:
            break
    return user_loan_choice


def add_choice():
    user_choice = None
    while True:
        user_choice = input('What would you like to add:\n'
                            'To add a book insert 1\n'
                            'To add a customer insert 2:\n'
                            '')
        if user_choice not in ("1", "2", '#'):
            print('Your can only choose between 1 or 2. Try again ')
        else:
            break
    return user_choice


def find_choice():
    user_choice = None
    while True:
        user_choice = input(('To find a book by his name insert 1:\n'
                             'To find a book by his author insert 2:\n'
                             ''))
        if user_choice not in ("1", "2", '#'):
            print(print('Your can only choose between 1 or 2. Try again '))
        else:
            break
    return user_choice


def find_by_first_or_last_name(search_value: str) -> str:
    print(f'You can find the {search_value} by entering author first name of last.')
    while True:
        search_result = input(f'Enter {search_value} first name of last: ').lower()
        if library_test.useful_function.is_str_valid(search_result) is False:
            print('Try again.')
        else:
            break
    return search_result


def start_library():
    while True:
        library_name = input('Enter your library name: ')
        city_library = input('Enter you library city: ')

        if useful_function.is_str_valid(library_name) is False or useful_function.is_str_valid(city_library) is False:
            print('please try again.')
        else:
            library = library_class.Library(library_name, city_library)
            break
    return library
