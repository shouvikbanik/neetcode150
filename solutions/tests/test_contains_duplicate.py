from unittest import TestCase

from solutions.contains_duplicate import contains_duplicate


class TestSolution(TestCase):
    def test_contains_duplicate_negative(self):
        nums = [1, 8, 3, 8, 7]
        return_value = contains_duplicate(nums)
        self.assertEqual(True, return_value)

    def test_contains_duplicate_positive(self):
        nums = [1, 4, 2, 6, 8, 0]
        return_value = contains_duplicate(nums)
        self.assertEqual(False, return_value)
