# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = defaultdict(list)
        def dfs(root):
            if not root:
                return 0

            if root in memo:
                return memo[root]

            included = root.val
            if root.left:
                included += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                included += dfs(root.right.left) + dfs(root.right.right)
            
            skip = dfs(root.left) + dfs(root.right)

            memo[root] = max(included, skip)

            return memo[root]
        
        return dfs(root)

        # def dfs_v1(root):
        #     nonlocal subSum

        #     if not root:
        #         return [0, 0]
        #     # left 和 right 都回傳有包含和沒包含的值
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     subSum = left[1] + right[1]
        #     directChildren = left[0] + right[1]
            
        #     # 要 left + right 就要捨棄自身
        #     # 要自身就可以取得 left.sub + right.sub
        #     # 0: 包含自己
        #     # 1: 不包含自己
        #     return [root.val + subSum, directChildren]
