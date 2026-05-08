# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    global maxD

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        def dfs(node, depth):
            depth += 1
            self.maxD = max(depth, self.maxD)

            if node.left:
                dfs(node.left, depth)
            if node.right:
                dfs(node.right, depth)

        node = root
        self.maxD, depth = 0, 0
        dfs(node, depth)

        return self.maxD