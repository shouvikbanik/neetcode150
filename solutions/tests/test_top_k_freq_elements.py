from unittest import TestCase

from top_k_freq_elements import top_k_frequent


class Test(TestCase):
    def test_top_k_frequent(self):
        self.assertEqual([6, 5, 3], top_k_frequent([1, 3, 3, 5, 5, 5, 6, 6, 6, 6], 3))

    def test_top_k_frequent2(self):
        self.assertEqual([-1, 2], top_k_frequent([4, 1, -1, 2, -1, 2, 3], 2))
