# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 1
        currentMax = root.val

        def dfs(currentMax, current):
            nonlocal count
            if currentMax <= current.val:
                count += 1
            currentMax = max(currentMax, current.val)
            if current.left:
                dfs(currentMax, current.left)
            if current.right:
                dfs(currentMax, current.right)

        if root.left:
            dfs(currentMax, root.left)
        if root.right:
            dfs(currentMax, root.right)

        return count