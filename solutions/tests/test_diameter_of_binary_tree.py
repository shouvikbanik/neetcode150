from unittest import TestCase

from diameter_of_binary_tree import diameter_of_binary_tree


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Test(TestCase):
    def test_diameter_of_binary_tree(self):
        node_root = self.create_binary_tree()
        self.assertEqual(3, diameter_of_binary_tree(node_root))

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
