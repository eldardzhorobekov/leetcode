# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def areSymmetric(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left or not right:
                return not left and not right
            if left.val != right.val:
                return False
            return (
                areSymmetric(left.left, right.right) and
                areSymmetric(left.right, right.left)
            )
        if not root:
            return True
        return areSymmetric(root.left, root.right)
