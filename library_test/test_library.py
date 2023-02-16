import datetime
import unittest
from library_backend import address_class
import library_backend.library_class
from frontend import input_function
from library_backend import exception


class CustomerClassTest(unittest.TestCase):
    def setUp(self) -> None:
        self.customer1 = library_backend.library_class.Customer('123456789', {"last_name": "cohen",
                                                                         "first_name": "noam"},
                                                           address_class.Address('lehi', "ofkim", '80300', "11")
                                                           , "noam.noam@gmail.com", '06.02.1983')

    def tearDown(self) -> None:
        pass

    def test_customer_class(self):
        self.assertEqual(self.customer1.get_customer_id(), '123456789')
        self.assertEqual(self.customer1.get_customer_first_name(), 'noam')
        self.assertEqual(self.customer1.get_customer_last_name(), 'cohen')
        self.assertEqual(self.customer1.get_email(), 'noam.noam@gmail.com')
        self.assertEqual(self.customer1.get_birth_day(), '06.02.1983')
        self.assertIsNone(self.customer1.set_email('noamcohen@gmail.com'))
        self.assertRaises(exception.NotValidEmail, self.customer1.set_email, 'noamnoamgmail.com')


class BookClassTest(unittest.TestCase):

    def setUp(self) -> None:
        self.book1 = library_backend.library_class.Book('123456789', 'orphan x', {'first_name': 'gregg',
                                                                                   'last_name': 'hurwitz'}, '2002', '3')
        self.book2 = library_backend.library_class.Book('987654321', 'lost son', {'first_name': 'gregg',
                                                                                   'last_name': 'hurwitz'}, '2019', '3')
        self.book3 = library_backend.library_class.Book('963258741', 'orphan x', {'first_name': 'gregg',
                                                                                   'last_name': 'hurwitz'}, '2002', '2')
        self.book4 = library_backend.library_class.Book('741852963', 'enders game', {'first_name': 'orson',
                                                                                      'last_name': 'scott card'},
                                                         '1994', '1')

    def tearDown(self) -> None:
        pass

    def test_book_class(self):
        self.assertEqual(self.book1.get_book_id(), '123456789')
        self.assertEqual(self.book4.get_book_name(), 'enders game')
        self.assertEqual(self.book3.get_author_first_name(), 'gregg')
        self.assertEqual(self.book2.get_author_last_name(), 'hurwitz')
        self.assertEqual(self.book2.get_type_of_loan(), '3')
        self.assertEqual(self.book3.get_year_published(), '2002')


class LoanClassTest(unittest.TestCase):

    def setUp(self) -> None:
        self.loan_date = datetime.datetime.now()
        self.loan_date_return = self.loan_date + datetime.timedelta(days=6)
        self.loan1 = library_backend.library_class.Loan("123456789", '987654321', self.loan_date, '2')

    def tearDown(self) -> None:
        pass

    def test_loan_class(self):
        self.assertEqual(self.loan1.get_loan_date(), self.loan_date)
        self.assertEqual(self.loan1.get_book_id(), '987654321')
        self.assertEqual(self.loan1.get_customer(), '123456789')
        self.assertEqual(self.loan1.get_max_return_date(), self.loan_date_return)
        self.assertIsNone(self.loan1.get_return_date())


class LibraryClassTest(unittest.TestCase):

    def setUp(self) -> None:
        self.library_1 = library_backend.library_class.Library('monty python', 'beer sheva')
        self.loan_date = datetime.datetime.now()
        self.loan_date_return = self.loan_date + datetime.timedelta(days=6)
        self.loan1 = library_backend.library_class.Loan("123456789", '987654321', self.loan_date, '2')
        self.book1 = library_backend.library_class.Book('123456789', 'orphan x', {'first_name': 'gregg',
                                                                                  'last_name': 'hurwitz'}, '2002', '3')
        self.book2 = library_backend.library_class.Book('987654321', 'lost son', {'first_name': 'gregg',
                                                                                  'last_name': 'hurwitz'}, '2019', '3')
        self.book3 = library_backend.library_class.Book('963258741', 'orphan x', {'first_name': 'gregg',
                                                                                  'last_name': 'hurwitz'}, '2002', '2')
        self.book4 = library_backend.library_class.Book('741852963', 'enders game', {'first_name': 'orson',
                                                                                     'last_name': 'scott card'},
                                                        '1994', '1')
        self.customer1 = library_backend.library_class.Customer('123456789', {"last_name": "cohen",
                                                                              "first_name": "noam"},
                                                                address_class.Address('lehi', "ofkim", '80300', "11")
                                                                , "noam.noam@gmail.com", '06.02.1983')

    def test_library(self):
        self.assertTrue(self.library_1.add_book(self.book1))
        self.assertTrue(self.library_1.add_customer(self.customer1))

    def test_start_library(self):
        self.library_1.add_book(self.book1)
        self.library_1.add_customer(self.customer1)
        result = input_function.start_library()
        self.assertIs(type(result), library_backend.library_class.Library)
        # self.assertRaises(BookAlreadyLoaned, Library.loan_book, self.library_1, self.book1)
        self.assertTrue(self.library_1.loan_book('123456789', '123456789'))





if __name__ == '__main__':
    unittest.main()
