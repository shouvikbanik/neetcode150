class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root == None:
        return None
    else:
        if root.right != None:
            temp_node = TreeNode(root.right.val)
            temp_node.left = root.right.left
            temp_node.right = root.right.right
        else:
            temp_node = None
        root.right = invert_tree(root.left)
        root.left = invert_tree(temp_node)
        return root
