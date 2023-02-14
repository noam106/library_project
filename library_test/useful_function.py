import re
import datetime
from library_backend import customer_code
from library_backend import address_class
from library_backend import exception
import time


def isvalid_email(email) -> bool:
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def is_valid_name(name_str: str) -> bool:
    if re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name_str):
        return True
    else:
        return False


def is_valid_bday(user_bday: str) -> bool:
    if re.search('^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$', user_bday):
        return True
    else:
        return False


def is_digit(str_to_check: str) -> bool:
    if re.fullmatch('[0-9]*', str_to_check):
        return True
    else:
        return False


def is_str_valid(str_to_check: str):
    if re.fullmatch('[A-Za-z ]*', str_to_check):
        return True
    else:
        return False


def let_me_read(sec):
    time.sleep(sec)



# def create_address():
#     while True:
#         customer_address_city = input('Insert customer city address: ')
#         customer_address_street = input('Insert customer street address: ')
#         customer_house_num = input('Insert customer house number: ')
#         customer_zipcode = input('Insert customer zipcode: ')
#
#         if is_digit(customer_zipcode) is False or is_digit(customer_house_num) is False or is_str_valid(customer_address_street) is False or is_str_valid(customer_address_city) is False:
#             print('one of your inputs is not valid, please try again: ')
#         else:
#             break
#
#     customer_address = address_class.Address(customer_address_street, customer_address_city,
#                                                      customer_zipcode,customer_house_num)
#     print('address created')
#     return customer_address
# print(is_valid_bday('12/13/5454'))


