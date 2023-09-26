from unittest import TestCase

from solutions.valid_anagram import is_anagram


class Test(TestCase):
    def test_is_anagram_positive(self):
        self.assertEqual(is_anagram("truck","cutrk"),True)
    def test_is_anagram_negative(self):
        self.assertEqual(is_anagram("truck","ck"),False)