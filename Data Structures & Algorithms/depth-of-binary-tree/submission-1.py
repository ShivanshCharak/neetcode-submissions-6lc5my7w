# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        length = 0
        def dfs(root,length):
            if not root:
                return 0
            length  = max(dfs(root.left,length), dfs(root.right, length)) + 1
            return length
        return dfs(root,0)


        