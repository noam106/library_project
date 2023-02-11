import datetime

import library_backend.address_class
from library_test import useful_function


class Customer:
    def __init__(self, customer_id: str, customer_name: dict, address: library_backend.address_class.Address,
                 email: str, birth_day: str):
        self._birth_day = birth_day
        self._email = email
        self._address = address
        self._customer_name = customer_name
        self._customer_id = customer_id

    def __str__(self):
        return f'{self._customer_name["last_name"]} {self._customer_name["first_name"]}, id number: {self._customer_id}'

    def __repr__(self):
        return self._customer_id, self._customer_name

    def get_birth_day(self):
        return self._birth_day

    def get_email(self):
        return self._email

    def set_email(self, new_email: str):
        if useful_function.isvalid_email(new_email):
            self._email = new_email

    def get_address(self):
        return self._address

    def get_customer_name(self):
        return self._customer_name

    def get_customer_first_name(self):
        return self._customer_name['first_name']

    def get_customer_last_name(self):
        return self._customer_name['last_name']

    def get_customer_id(self):
        return self._customer_id
