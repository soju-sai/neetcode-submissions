# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        longest = 0
        def dfs(root, parentVal, count):
            nonlocal longest
            if not root:
                # longest = max(count, longest)
                return 

            if root.val == parentVal + 1:
                count += 1
                longest = max(count, longest)
            else:
                longest = max(count, longest)
                count = 1

            # longest = max(count, longest)
            dfs(root.left, root.val, count)
            dfs(root.right, root.val, count)

        dfs(root, root.val - 1, 0)
        return longest

