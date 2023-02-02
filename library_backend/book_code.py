import datetime
import re

import library_test.useful_function
from library_test import *


class Book:
    def __init__(self, book_id: str, book_name: str, author: dict, year_publish: datetime, type_of_loan: int):
        self._type_of_loan = type_of_loan
        self._year_publish = datetime.datetime.strptime(year_publish, '%y')
        self._author = author
        self._book_name = book_name
        self._book_id = book_id
        self._type_of_loan = type_of_loan

    def get_type_of_loan(self):
        return self._type_of_loan

    def set_type_of_loan(self, new_type: int):
        self._type_of_loan = new_type

    def get_year_published(self):
        return self._year_publish

    def get_author(self):
        return self._author

    def get_book_name(self):
        return self._book_name

    def get_book_id(self):
        return self._book_id


class Customer:
    def __init__(self, customer_id: int, customer_name: dict, address: classmethod, email: str, birth_day: datetime):
        self._birth_day = birth_day
        self._email = email
        self._address = address
        self._customer_name = customer_name
        self._customer_id = customer_id

    def get_birth_day(self):
        return self._birth_day

    def get_email(self):
        return self._email

    def set_email(self, new_email: str):
        if library_test.useful_function.isvalid_email(new_email):
            self._email = new_email

    def get_address(self):
        return self._address

    def get_customer_name(self):
        return self._customer_name

    def get_customer_id(self):
        return self._customer_id


class Loan:
    def __init__(self, costumer_id: int, book_id: int, loan_date: datetime):
        self._costumer_id = costumer_id
        self._book_id = book_id
        self._loan_date = loan_date




