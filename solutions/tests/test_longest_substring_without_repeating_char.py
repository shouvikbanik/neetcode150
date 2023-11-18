from unittest import TestCase

from longest_substring_without_repeating_char import length_of_longest_substring


class Test(TestCase):
    def test_length_of_longest_substring(self):
        self.assertEqual(3, length_of_longest_substring("pwwkew"))
