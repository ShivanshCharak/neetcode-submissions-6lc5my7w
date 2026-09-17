# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodOnes = 0
        def dfs(root, lastSaw):
            nonlocal goodOnes
            if not root:
                return None
            if root.val >= lastSaw:
                lastSaw = root.val
                goodOnes += 1 
            dfs(root.left, lastSaw)
            dfs(root.right, lastSaw)
        dfs(root, root.val)
        return goodOnes
