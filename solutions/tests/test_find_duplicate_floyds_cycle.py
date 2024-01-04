from unittest import TestCase

from find_duplicate_floyds_cycle import find_duplicate


class Test(TestCase):
    def test_find_duplicate(self):
        self.assertEqual(4, find_duplicate([1, 3, 4, 2, 4]))
