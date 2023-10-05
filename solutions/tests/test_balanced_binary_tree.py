from unittest import TestCase

from balanced_binary_tree import is_balanced


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Test(TestCase):
    def test_is_balanced_positive(self):
        root = self.create_balanced_binary_tree()
        self.assertEqual(is_balanced(root), True)

    def test_is_balanced_negative(self):
        root = self.create_unbalanced_binary_tree()
        self.assertEqual(is_balanced(root), False)

    def create_balanced_binary_tree(self):
        node1 = TreeNode(3)
        node2 = TreeNode(9)
        node3 = TreeNode(20)
        node4 = TreeNode(15)
        node5 = TreeNode(7)
        node1.left = node2
        node1.right = node3
        node3.left = node4
        node3.right = node5
        return node1

    def create_unbalanced_binary_tree(self):
        node1 = TreeNode(3)
        node2 = TreeNode(9)
        node3 = TreeNode(20)
        node1.right = node2
        node2.right = node3
        return node1
