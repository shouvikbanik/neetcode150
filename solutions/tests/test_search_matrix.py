from unittest import TestCase

from search_matrix import search_matrix


class Test(TestCase):
    def test_search_matrix(self):
        self.assertEqual(True, search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
