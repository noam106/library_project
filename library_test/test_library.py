import unittest
from library_backend import address_class
import library_backend.library_class
from frontend import input_function


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
        self.assertEqual(self.customer1.)


    def test_start_library(self):
        result = input_function.start_library()
        self.assertIs(type(result), library_backend.library_class.Library)




if __name__ == '__main__':
    unittest.main()
