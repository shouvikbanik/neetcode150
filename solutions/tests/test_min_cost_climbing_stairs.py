from unittest import TestCase

from min_cost_climbing_stairs import min_cost_climbing_stairs


class Test(TestCase):
    def test_min_cost_climbing_stairs(self):
        self.assertEqual(6, min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
