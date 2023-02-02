from book_code import *


class Library:
    def __init__(self, library_name: str, address: classmethod):
        self._address = address
        self._library_name = library_name
        self._books: dict[str, Book] = {}
        self._costumer: dict[str, Customer] = {}