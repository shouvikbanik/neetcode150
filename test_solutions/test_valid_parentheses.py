from unittest import TestCase

from valid_parentheses import is_valid


class Test(TestCase):
    def test_is_valid_negative(self):
        self.assertEqual(is_valid("{{{}"), False)

    def test_is_valid_positive(self):
        self.assertEqual(is_valid("{{{}}}"), True)
