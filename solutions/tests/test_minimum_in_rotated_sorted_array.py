from unittest import TestCase

from minimum_in_rotated_sorted_array import find_min


class Test(TestCase):
    def test_find_min(self):
        self.assertEqual(1, find_min([3, 4, 5, 1, 2]))
