from unittest import TestCase

from climbing_stairs import climb_stairs


class Test(TestCase):
    def test_climb_stairs(self):
        self.assertEqual(climb_stairs(3), 3)
