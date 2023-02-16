class LibraryException(Exception):
    pass


class BookExistsError(LibraryException):
    def __init__(self, book_num: str):
        super().__init__()
        self._book_num = book_num


class BookAlreadyLoaned(LibraryException):
    def __init__(self, book_id: str):
        super().__init__()
        self._book_id = book_id


class LateReturnPunishment(LibraryException):
    def __init__(self, customer_id):
        super().__init__()
        self._customer_id = customer_id


class CustomerExistsError(LibraryException):
    def __init__(self, customer_id: str):
        super().__init__()
        self._customer_id = customer_id


class NotNumber(LibraryException):
    def __init__(self, string: str):
        super().__init__()
        self._strint = string


class NotValidString(LibraryException):
    def __init__(self, string: str):
        super().__init__()
        self._string = string


class NotValidDate(LibraryException):
    def __init__(self, date_str: str):
        super().__init__()
        self._date_string = date_str


class  NotValidEmail(LibraryException):
    pass


class CantRemoveCustomer(LibraryException):
    def __init__(self, customer_id: str):
        super().__init__()
        self._customer_id = customer_id

