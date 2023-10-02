from unittest import TestCase

from plus_one import plus_one


class Test(TestCase):
    def test_plus_one(self):
        self.assertEqual(plus_one([1, 2, 9]), [1, 3, 0])
