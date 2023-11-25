from unittest import TestCase

from container_with_most_water import max_area


class Test(TestCase):
    def test_max_area(self):
        self.assertEqual(49, max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
