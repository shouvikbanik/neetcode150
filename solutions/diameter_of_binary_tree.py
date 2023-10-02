from max_depth_binary_tree import max_depth


def diameter_of_binary_tree(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root == None or (root.left == None and root.right == None):
        return 0
    else:
        return max(max_depth(root.left) + max_depth(root.right), diameter_of_binary_tree(root.left),
                   diameter_of_binary_tree(root.right))
