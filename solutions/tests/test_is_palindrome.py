from unittest import TestCase

from solutions.is_palindrome import is_palindrome


class Test(TestCase):
    def test_is_palindrome_positive(self):
        self.assertEqual(is_palindrome("r,aceCar"), True)

    def test_is_palindrome_negative(self):
        self.assertEqual(is_palindrome("rhasld_Cnm"), False)
