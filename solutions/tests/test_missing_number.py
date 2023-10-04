from unittest import TestCase

from missing_number import missing_number


class Test(TestCase):
    def test_missing_number(self):
        self.assertEqual(missing_number([0, 3, 4, 2]), 1)
