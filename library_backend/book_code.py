import datetime
import re
from library_class import *
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







