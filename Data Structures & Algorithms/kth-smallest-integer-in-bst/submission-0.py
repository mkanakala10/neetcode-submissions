# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def inorder(curr) -> None:
            if not curr:
                return
            
            if curr.left:
                inorder(curr.left)

            res.append(curr.val)

            if curr.right:
                inorder(curr.right)

        inorder(root)
        return res[k - 1]