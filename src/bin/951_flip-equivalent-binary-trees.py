#
# @lc app=leetcode id=951 lang=python3
#
# [951] Flip Equivalent Binary Trees
#


class TreeNode:
    def __init__(
        self, val: int = 0, left: Optional[Self] = None, right: Optional[Self] = None
    ):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, Self


def sort_children(root: TreeNode):
    if (root.left and not root.right) or (
        root.left and root.right and root.left.val > root.right.val
    ):
        root.left, root.right = root.right, root.left


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if bool(root1) != bool(root2):
            return False
        if not root1 and not root2:
            return True
        assert root1 and root2
        if root1.val != root2.val:
            return False
        sort_children(root1)
        sort_children(root2)
        return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(
            root1.right, root2.right
        )


# @lc code=end
