from unittest import TestCase
from binary_search import search


class Test(TestCase):
    def test_search(self):
        self.assertEqual(4, search([-1, 0, 3, 5, 9, 12], 9))
