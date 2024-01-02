from unittest import TestCase

from reverse_int import reverse


class Test(TestCase):
    def test_reverse(self):
        self.assertEqual(-123, reverse(-321))
