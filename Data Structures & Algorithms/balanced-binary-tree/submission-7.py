# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [0, True]
            left = dfs(root.left)
            right = dfs(root.right)
            diff = abs(left[0] -right[0])
            length = max(left[0] , right[0]) +1
            if diff > 1:
                return [length, False]
            elif diff <= 1:
                return [length, left[1] and right[1]]
        return dfs(root)[1]
        
        