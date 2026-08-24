# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # height 是從最底的 leaf 出發，最底是0，慢慢往上加
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return [True, 0]
            
            left, right = dfs(node.left), dfs(node.right)
            balanced = left[0] and right[0] and (abs(left[1] - right[1]) < 2)
            height = 1 + max(left[1], right[1])
            return [balanced, height]

        return dfs(root)[0]

    # 只比整個母樹的左右子樹是否balanced
    def isBalanced_v1(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        level = 1

        def dfs(node, level):
            if node is None:
                return level
            
            level = max(dfs(node.left, level), dfs(node.right, level))
            level += 1

            return level

        return True if abs(dfs(root.left, level) - dfs(root.right, level)) <= 1 else False
