from unittest import TestCase

from plus_one import plus_one


class Test(TestCase):
    def test_plus_one(self):
        self.assertEqual([1, 3, 0], plus_one([1, 2, 9]))
