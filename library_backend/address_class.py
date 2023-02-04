class Address:

    def __init__(self, street: str, city: str, zipcode: str, house_num: str):
        self._street = street
        self._city = city
        self._house_num = house_num
        self._zipcode = zipcode

    def get_street(self):
        return self._street

    def get_city(self):
        return self._city

    def get_house_num(self):
        return self._house_num

    def get_zipcode(self):
        return self._zipcode
