def is_same_tree(tree, subtree):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if tree is None and subtree is None:
        return True
    elif tree is None and subtree:
        return False
    elif tree and subtree is None:
        return False
    elif tree.val != subtree.val:
        return False
    else:
        return is_same_tree(tree.left, subtree.left) and is_same_tree(tree.right, subtree.right)


def is_subtree(root, subroot):
    """
    :type root: TreeNode
    :type subRoot: TreeNode
    :rtype: bool
    """
    subtree = False
    if root:
        if root.right:
            subtree |= is_subtree(root.right, subroot)
        if root.left:
            subtree |= is_subtree(root.left, subroot)
        subtree |= is_same_tree(root, subroot)
        return subtree
    else:
        return False
