from unittest import TestCase

from valid_parentheses import is_valid


class Test(TestCase):
    def test_is_valid_negative(self):
        self.assertEqual(False, is_valid("{{{}"))

    def test_is_valid_positive(self):
        self.assertEqual(True, is_valid("{{{}}}"))
