from unittest import TestCase

from invert_binary_tree import invert_tree


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Test(TestCase):
    def test_invert_tree(self):
        root = self.create_binary_tree()
        result = self.get_list_from_tree(invert_tree(root))
        self.assertEqual([3, 20, 7, 15, 9], result)

    def get_list_from_tree(self, node):
        if node == None:
            return []
        else:
            left_subtree = self.get_list_from_tree(node.left)
            right_subtree = self.get_list_from_tree(node.right)
            return [node.val] + left_subtree + right_subtree

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
