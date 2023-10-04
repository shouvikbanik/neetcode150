from unittest import TestCase

from counting_bits import count_bits


class Test(TestCase):
    def test_count_bits(self):
        self.assertEqual(count_bits(5), [0, 1, 1, 2, 1, 2])
