from unittest import TestCase

from best_time_to_buy_and_sell_stock import max_profit


class Test(TestCase):
    def test_max_profit(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)
