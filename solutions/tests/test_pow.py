from unittest import TestCase

from pow import my_pow


class Test(TestCase):
    def test_my_pow(self):
        self.assertEqual(0.00, my_pow(0.00001, 2147483647))
