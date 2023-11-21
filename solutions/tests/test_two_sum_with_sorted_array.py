from unittest import TestCase

from two_sum_with_sorted_array import two_sum_on_sorted_array


class Test(TestCase):
    def test_two_sum_on_sorted_array(self):
        self.assertEqual([1, 2], two_sum_on_sorted_array([2, 7, 11, 15], 9))
