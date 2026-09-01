# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0

    def goodNodes(self, root: TreeNode) -> int:
        currentMax = root.val

        def dfs(currentMax, current):
            if not current:
                return None
            
            if currentMax <= current.val:
                self.count += 1
            currentMax = max(currentMax, current.val)
            dfs(currentMax, current.left)        
            dfs(currentMax, current.right)
            
        dfs(currentMax, root)
        return self.count

    def goodNodes_v1(self, root: TreeNode) -> int:
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