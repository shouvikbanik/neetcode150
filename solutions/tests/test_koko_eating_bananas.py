from unittest import TestCase

from koko_eating_bananas import min_eating_speed


class Test(TestCase):
    def test_min_eating_speed(self):
        self.assertEqual(4, min_eating_speed([3, 6, 7, 11], 8))
