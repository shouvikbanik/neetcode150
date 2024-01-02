from unittest import TestCase

from spiral_order import spiral_order


class Test(TestCase):
    def test_spiral_order(self):
        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
