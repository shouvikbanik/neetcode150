from unittest import TestCase

from longest_repeating_character_replacement import character_replacement


class Test(TestCase):
    def test_character_replacement(self):
        self.assertEqual(4, character_replacement("AABABBA", 1))

    def test_character_replacement2(self):
        self.assertEqual(4, character_replacement("ABAB", 2))
