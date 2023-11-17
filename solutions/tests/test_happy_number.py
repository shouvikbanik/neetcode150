from unittest import TestCase

from happy_number import is_happy


class Test(TestCase):
    def test_is_happy_positive(self):
        self.assertEqual(True, is_happy(7))

    def test_ishappy_negative(self):
        self.assertEqual(False, is_happy(2))
