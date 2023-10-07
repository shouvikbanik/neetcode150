from unittest import TestCase

from last_stone_weight import last_stone_weight


class Test(TestCase):
    def test_last_stone_weight(self):
        self.assertEqual(last_stone_weight([2, 7, 4, 1, 8, 1]), 1)
