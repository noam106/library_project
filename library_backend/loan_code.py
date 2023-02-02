import datetime
class Loan:
    def __init__(self, costumer_id: str, book_id: str, loan_date: datetime):
        self._costumer_id = costumer_id
        self._book_id = book_id
        self._loan_date = loan_date

    def time_loan_2_max_days(self) -> datetime:
        if Library.get_books().[self._book_id] == 1:
            max_time_loan = datetime.timedelta(days=10)
        elif type_loan == 2:
            max_time_loan = datetime.timedelta(days=5)
        else:
            max_time_loan = datetime.timedelta(days=2)
        return max_time_loan
