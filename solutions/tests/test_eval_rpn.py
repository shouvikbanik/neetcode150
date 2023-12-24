from unittest import TestCase

from eval_rpn import eval_rpn


class Test(TestCase):
    def test_eval_rpn(self):
        self.assertEqual(22, eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
