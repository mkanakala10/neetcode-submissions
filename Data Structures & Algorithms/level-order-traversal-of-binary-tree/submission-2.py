# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 0)])
        res = []
        temp = []
        curr_level = 0
        while queue:
            
            curr, level = queue.popleft()

            if curr_level != level:
                res.append(temp)
                temp = []
                curr_level = level
            temp.append(curr.val)
            if curr.left:
                queue.append((curr.left, level + 1))
            if curr.right:
                queue.append((curr.right, level + 1))
        if temp:
            res.append(temp)
        return res



