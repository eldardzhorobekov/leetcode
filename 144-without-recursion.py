# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = [root]
        res = []
        while st:
            top_node = st.pop()
            if not top_node:
                continue
            res.append(top_node.val)
            st.append(top_node.right)
            st.append(top_node.left)
        return res
