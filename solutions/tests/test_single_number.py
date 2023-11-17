from unittest import TestCase

from single_number import single_number


class Test(TestCase):
    def test_single_number(self):
        self.assertEqual(2, single_number([1, 2, 3, 1, 3]))
