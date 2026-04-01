# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depthP = 1
        def dfs(node, depth):

            if not node:
                return depth - 1

            nodeleft = dfs(node.left, depth + 1)
            noderight = dfs(node.right, depth + 1)
            return max(nodeleft, noderight)
        
        return dfs(root, depthP)

        