import datetime

if __name__ == '__main__':
    print('hello there, before we start')
    while True:
        print('In any time you wish to leave the program insert: "#"')
        user_choice = input('What would you like to do?\n'
                            'To add a new customer or new book insert "1"\n'
                            'To Loan or return a book insert "2"\n'
                            'To display information of loans, books, or customer insert "3"\n'
                            'To remove a book or customer from library insert "4"\n'
                            'To find a book insert "5"\n'
                            'To find a customer insert "6"\n'
                            'Insert your choice here:\n')
        if user_choice not in ('1', '2', '3', '4', '5', '6', '#'):
            print('your choice is invalid, please try again: \n')
        else:
            break
