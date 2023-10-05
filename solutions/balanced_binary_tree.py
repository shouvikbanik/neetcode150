def is_balanced_helper(root):
    if root == None:
        return True, 0
    else:
        is_right_subtree_balanced, height_of_right_subtree = is_balanced_helper(root.right)
        is_left_subtree_balanced, height_of_left_subtree = is_balanced_helper(root.left)
        if is_left_subtree_balanced and is_right_subtree_balanced and abs(
                height_of_left_subtree - height_of_right_subtree) < 2:
            return True, 1 + max(height_of_right_subtree, height_of_left_subtree)
        return False, 1 + max(height_of_right_subtree, height_of_left_subtree)


def is_balanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    return is_balanced_helper(root)[0]
