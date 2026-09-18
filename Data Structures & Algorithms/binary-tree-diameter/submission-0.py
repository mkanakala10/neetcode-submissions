# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.high = 0
        def dfs(root):
            if not root:
                return 0
            resleft = dfs(root.left)
            resright = dfs(root.right)
            self.high = max(self.high, resleft + resright)
            return max(resleft, resright) + 1
        dfs(root)
        return self.high
        