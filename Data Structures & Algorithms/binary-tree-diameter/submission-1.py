# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    maxDiameter = 0

    def dfs(node):
      nonlocal maxDiameter
      if not node:
        return 0

      leftHeight = dfs(node.left)
      rightHeight = dfs(node.right)

      height = max(leftHeight, rightHeight)
      maxDiameter = max(maxDiameter, leftHeight + rightHeight)

      return 1 + height

    dfs(root)

    return maxDiameter
