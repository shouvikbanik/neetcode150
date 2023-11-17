from unittest import TestCase

from solutions.valid_anagram import is_anagram


class Test(TestCase):
    def test_is_anagram_positive(self):
        self.assertEqual(True, is_anagram("truck", "cutrk"))

    def test_is_anagram_negative(self):
        self.assertEqual(False, is_anagram("truck", "ck"))
