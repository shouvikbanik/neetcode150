from unittest import TestCase
from subtree_of_another_tree import is_subtree


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Test(TestCase):
    def test_is_subtree_positive(self):
        tree_root = self.create_binary_tree()
        subtree_root = self.create_subtree()
        self.assertEqual(is_subtree(tree_root, subtree_root), True)

    def test_is_subtree_negative(self):
        subtree_root = self.create_subtree()
        self.assertEqual(is_subtree(None, subtree_root), False)

    def create_binary_tree(self):
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

    def create_subtree(self):
        node1 = TreeNode(20)
        node2 = TreeNode(15)
        node3 = TreeNode(7)
        node1.left = node2
        node1.right = node3
        return node1