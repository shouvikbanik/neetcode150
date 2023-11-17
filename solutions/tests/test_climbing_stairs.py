from unittest import TestCase

from climbing_stairs import climb_stairs


class Test(TestCase):
    def test_climb_stairs(self):
        self.assertEqual(3, climb_stairs(3))
