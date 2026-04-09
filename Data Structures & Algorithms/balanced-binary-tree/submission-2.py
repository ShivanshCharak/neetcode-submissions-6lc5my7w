# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [0,True]
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left[0] - right[0])>1 or not left[1] or not right[1]:
                return [left[0]-right[0],False]
            return [max(left[0],right[0])+1,True]
        return dfs(root)[1]
        
                
        
        