# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            curr, low, hi = stack.pop()

            if curr.left:
                if low < curr.left.val < curr.val:
                    stack.append((curr.left, low, curr.val))
                else:
                    return False
            if curr.right:
                if hi > curr.right.val > curr.val:
                    stack.append((curr.right, curr.val, hi))
                else:
                    return False
        return True
