from unittest import TestCase

from solutions.two_sum import two_sum


class Test(TestCase):
    def test_two_sum(self):
        return_val = two_sum([2, 7, 4, 3], 9)
        self.assertEqual({0, 1}, return_val)
