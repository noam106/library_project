import datetime


def time_loan_2_max_days(loan_type: int) -> datetime:
    if loan_type == 1:
        max_time_loan = datetime.timedelta(days=10)
    elif loan_type == 2:
        max_time_loan = datetime.timedelta(days=5)
    else:
        max_time_loan = datetime.timedelta(days=2)
    return max_time_loan


class Loan:
    def __init__(self, costumer_id: str, book_id: str, loan_date: datetime, loan_type: int):
        self._costumer_id = costumer_id
        self._book_id = book_id
        self._loan_date = loan_date
        self._return_date = loan_date + time_loan_2_max_days(loan_type)
        if datetime.date.weekday(self._return_date) == 4:
            self._return_date += datetime.timedelta(days=2)
        if datetime.date.weekday(self._return_date) == 5:
            self._return_date += datetime.timedelta(days=1)

    def __str__(self):
        return f'customer number {self._costumer_id} took book number {self._book_id}, return date: {self._return_date}'

    def __repr__(self):
        return f'customer number = {self._costumer_id}\n' \
               f'book number = {self._book_id}\n' \
               f'return date = {self._return_date}'

    def get_customer(self):
        return self._costumer_id

    def get_book_id(self):
        return self._book_id

    def get_return_date(self):
        return self._return_date

    def get_loan_date(self):
        return self._loan_date





