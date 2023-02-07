import library_backend.customer_code
from library_test import useful_function
from library_backend import library_class, address_class


def create_address():
    while True:
        customer_address_city = input('Insert customer city address: ')
        customer_address_street = input('Insert customer street address: ')
        customer_house_num = input('Insert customer house number: ')
        customer_zipcode = input('Insert customer zipcode: ')

        if useful_function.is_digit(customer_zipcode) is False or useful_function.is_digit(customer_house_num) is False or useful_function.is_str_valid(customer_address_street) is False or useful_function.is_str_valid(customer_address_city) is False:
            print('one of your inputs is not valid, please try again: ')
        else:
            break

    customer_address = address_class.Address(customer_address_street, customer_address_city,
                                                     customer_zipcode,customer_house_num)
    print('address created')
    return customer_address


def create_customer(customer_address):
    while True:
        customer_last_name = input('Insert customer last name: ')
        customer_first_name = input('Insert customer first name: ')
        customer_id = input('Insert customer id number: ')
        customer_email = input('Insert customer email: ')
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


def add_a_book():
    while True:
        book_id = input('Insert the book ID: ')
        book_name = input('Insert the book name: ')
        author_last_name = input('Insert author last name: ')
        author_first_name = input('Insert author first name: ')
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


def loan_a_book():
    book_id = input('Enter the the book ID number: ')
    customer_id = input('Enter customer ID number: ')


