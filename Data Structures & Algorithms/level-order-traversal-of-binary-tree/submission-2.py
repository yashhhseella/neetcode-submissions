# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []

        q = collections.deque() #deque to add from left and remove from right FILO
        q.append(root)

        while q:
            curLevelNodes = []

            for i in range(len(q)):
                node = q.popleft()

                if node:
                    curLevelNodes.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if curLevelNodes:
                res.append(curLevelNodes)
        return res
        