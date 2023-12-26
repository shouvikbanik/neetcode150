from unittest import TestCase

from multiply_strings import multiply


class Test(TestCase):
    def test_multiply(self):
        self.assertEqual("56088", multiply("123", "456"))
