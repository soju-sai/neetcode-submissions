# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 思考重點：
    # 1. 取得分支的總和，或是取得單邊分支的總和
    # 2. 遇到負數，持續加上去，回傳總和，反正最終運算過程中，會知道當下的最大總和
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 要有一個存最大值的變數
        self.pathSum = root.val

        # 回傳沒有分支的path sum
        def dfs(root):
            if not root:
                return 0

            # 取得左右樹的最大值
            maxLeft = dfs(root.left)
            maxRight = dfs(root.right)
            maxLeft = max(maxLeft, 0)
            maxRight = max(maxRight, 0)

            # 取得目前節點的左右分支的最大值
            self.pathSum = max(root.val + maxLeft + maxRight, self.pathSum)

            # 回傳有分支的最大值
            return max(root.val + maxLeft, root.val + maxRight, 0)

        dfs(root)

        return self.pathSum