from unittest import TestCase

from search_in_rotated_sorted_array import search


class Test(TestCase):
    def test_search(self):
        self.assertEqual(4, search([4, 5, 6, 7, 0, 1, 2], 0))
