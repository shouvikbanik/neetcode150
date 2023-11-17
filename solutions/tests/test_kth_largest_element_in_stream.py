from unittest import TestCase

from kth_largest_element_in_stream import KthLargest


class TestKthLargest(TestCase):
    def test_add(self):
        obj = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(4, obj.add(3))
        self.assertEqual(5, obj.add(5))
