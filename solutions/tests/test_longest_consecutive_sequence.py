from unittest import TestCase

from longest_consecutive_sequence import longest_consecutive


class Test(TestCase):
    def test_longest_consecutive(self):
        self.assertEqual(4, longest_consecutive([100, 4, 200, 1, 3, 2]))
