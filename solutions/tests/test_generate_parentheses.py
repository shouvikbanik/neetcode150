from unittest import TestCase

from generate_parentheses import generate_parentheses, generate_parentheses_helper


class Test(TestCase):
    def test_generate_parentheses(self):
        self.assertEqual(set(["((()))", "(()())", "(())()", "()(())", "()()()"]), generate_parentheses(3))

    def test_generate_parentheses_helper(self):
        self.assertEqual(set(["((()))", "(()())", "(())()", "()(())", "()()()"]),
                         set(generate_parentheses_helper(3, 0, 0, '', [])))
