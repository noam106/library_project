import re
import datetime

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def isvalid_email(email) -> bool:
    if re.fullmatch(regex, email):
        return True
    else:
        return False


# def time_loan_2_max_days(type_loan: int) -> datetime:
#     if type_loan not in (1, 2, 3):
#         raise  # write a raise condition
#     if type_loan == 1:
#         max_time_loan = datetime.timedelta(days=10)
#     elif type_loan == 2:
#         max_time_loan = datetime.timedelta(days=5)
#     else:
#         max_time_loan = datetime.timedelta(days=2)
#     return max_time_loan


def is_valid_name(name_str: str) -> bool:
    if re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name_str):
        return True
    else:
        return False


def is_valid_bday(user_bday: str) -> bool:
    if re.search(
        "^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)"
        "([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])$|^([0-9][0-9]|19[0-9][0-9]|20[0-9]"
        "[0-9])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])$",
        user_bday):
        return True
    else:
        False


def is_digit(str_to_check: str) -> bool:
    if re.fullmatch('[0-9]*', str_to_check):
        return True
    else:
        return False


def is_str(str_to_check: str) -> bool:
    if re.fullmatch('[A-Za-z]*', str_to_check):
        return True
    else:
        return False


# print(is_digit('159h9'))

# def date_to_return(days_to_loan: datetime) ->datetime:
