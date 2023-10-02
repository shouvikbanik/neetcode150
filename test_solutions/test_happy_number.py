from unittest import TestCase

from happy_number import is_happy


class Test(TestCase):
    def test_is_happy_positive(self):
        self.assertEqual(is_happy(7), True)

    def test_ishappy_negative(self):
        self.assertEqual(is_happy(2), False)
