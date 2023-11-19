from unittest import TestCase

from product_of_array_except_self import product_except_self


class Test(TestCase):
    def test_product_except_self(self):
        self.assertEqual([24, 12, 8, 6], product_except_self([1, 2, 3, 4]))
