import datetime
import re
import library_test.useful_function
from library_test import *


class Book:
    def __init__(self, book_id: str, book_name: str, author: dict, year_publish: str, type_of_loan: str):
        self._type_of_loan = type_of_loan
        self._year_publish = year_publish
        self._author = author
        self._book_name = book_name
        self._book_id = book_id
        self._type_of_loan = type_of_loan

    def __str__(self):
        return f'{self._book_name} by {self._author["last_name"]}, {self._author["first_name"]}'

    def __repr__(self):
        return f'{self._book_name} by {self._author["last_name"]}, {self._author["first_name"]}'

    def get_type_of_loan(self):
        return self._type_of_loan

    def set_type_of_loan(self, new_type: int):
        self._type_of_loan = new_type

    def get_year_published(self):
        return self._year_publish

    def get_author(self):
        return self._author

    def get_author_first_name(self):
        return self._author['first_name']

    def get_author_last_name(self):
        return self._author['last_name']

    def get_book_name(self):
        return self._book_name

    def get_book_id(self):
        return self._book_id







