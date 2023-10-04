from unittest import TestCase

from reverse_bits import reverse_bits


class Test(TestCase):
    def test_reverse_bits(self):
        self.assertEqual(964176192, reverse_bits(43261596))
