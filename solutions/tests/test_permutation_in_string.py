from unittest import TestCase

from permutation_in_string import check_inclusion


class Test(TestCase):
    def test_check_inclusion(self):
        self.assertEqual(True, check_inclusion("ab", "eidbaooo"))
