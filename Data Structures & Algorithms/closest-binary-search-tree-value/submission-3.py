# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = [float('inf'), None]
        
        def dfs(node, target):
            nonlocal closest
            if not node:
                return
            
            diff = abs(target - node.val)
            if diff < closest[0]:
                closest = [diff, node.val]

            if node.val < target:
                return dfs(node.right, target)
            if node.val > target:
                return dfs(node.left, target)
            else:
                return

        # def dfs_v1(node, t):
        #     nonlocal closest
        #     # print(node, last, t, closest)
        #     if not node:
        #         closest = last
        #         return last
        #     if t == node.val:
        #         closest = node.val
        #         return closest
        #     elif t > node.val:
        #         dfs(node.right, node.val, t)
        #     elif t < node.val:
        #         dfs(node.left, node.val, t)

        dfs(root, target)

        return closest[1]