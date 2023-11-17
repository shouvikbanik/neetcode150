from unittest import TestCase

from solutions.is_palindrome import is_palindrome


class Test(TestCase):
    def test_is_palindrome_positive(self):
        self.assertEqual(True, is_palindrome("r,aceCar"))

    def test_is_palindrome_negative(self):
        self.assertEqual(False, is_palindrome("rhasld_Cnm"))
