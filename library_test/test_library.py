import unittest

import library_backend.library_class
from frontend import input_function


class MyTestCase(unittest.TestCase):
    def test_start_library(self):
        result = input_function.start_library()
        self.assertIs(type(result), library_backend.library_class.Library)




if __name__ == '__main__':
    unittest.main()
