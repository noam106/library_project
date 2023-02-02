import library_test
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
