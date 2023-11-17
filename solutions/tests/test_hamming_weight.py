from unittest import TestCase

from hamming_weight import hamming_weight


class Test(TestCase):
    def test_hamming_weight(self):
        binary_string = '00000000000000000000000000001011'
        self.assertEqual(3, hamming_weight(11))
