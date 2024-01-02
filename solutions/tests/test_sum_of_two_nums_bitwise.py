from unittest import TestCase

from sum_of_two_nums_bitwise import get_sum


class Test(TestCase):
    def test_get_sum(self):
        self.assertEqual(20, get_sum(9, 11))
