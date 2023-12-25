from unittest import TestCase

from daily_temperatures import daily_temperatures


class Test(TestCase):
    def test_daily_temperatures(self):
        self.assertEqual([1, 1, 4, 2, 1, 1, 0, 0], daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
