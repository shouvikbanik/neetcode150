def max_depth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root == None:
        return 0
    else:
        return 1 + max(max_depth(root.left), max_depth(root.right))
