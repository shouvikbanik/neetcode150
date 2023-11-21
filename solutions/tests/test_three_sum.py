from unittest import TestCase

from three_sum import three_sum


class Test(TestCase):
    def test_three_sum(self):
        self.assertEqual([[-1, 0, 1]], three_sum([-1, 0, 1, 1, 0, -4]))

    def test_three_sum2(self):
        self.assertEqual([[0, 0, 0]], three_sum([0, 0, 0]))

    def test_three_sum3(self):
        self.assertEqual([], three_sum([0, 1, 1]))
