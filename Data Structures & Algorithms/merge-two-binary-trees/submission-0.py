# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    def dfs(r1, r2):
      if not r1 and not r2:
        return None

      v1 = r1.val if r1 else 0
      v2 = r2.val if r2 else 0
      root = TreeNode(v1 + v2)
      root.left = dfs(r1.left if r1 else None, r2.left if r2 else None)
      root.right = dfs(r1.right if r1 else None, r2.right if r2 else None)
      return root

    return dfs(root1, root2)

  def mergeTrees_v2(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    def dfs(r1, r2):
      if not r1 and not r2:
        return
      
      r1Val = r1.val if r1 else 0
      r2Val = r2.val if r2 else 0
      r3 = TreeNode(r1Val + r2Val)

      if not r1:
        if r2.left:
          r3.left = dfs(None, r2.left,)
        if r2.right:
          r3.right = dfs(None, r2.right)
      if not r2:
        if r1.left:
          r3.left = dfs(r1.left, None)
        if r1.right:
          r3.right = dfs(r1.right, None)
      else:
        r3.left = dfs(r1.left, r2.left)
        r3.right = dfs(r1.right, r2.right)

      return r3

    # root3 = TreeNode()
    return dfs(root1, root2)
    
    # return root3

  def mergeTrees_v1(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    root3 = TreeNode()
    
    def dfs(r1, r2, r3):
      r3.left, r3.right = TreeNode(), TreeNode()
      if r1 and r2:
        r3.val = r1.val + r2.val
        dfs(r1.left, r2.left, r3.left)
        dfs(r1.right, r2.right, r3.right)
        return
      elif r2:
        r3.val = r2.val
        dfs(None, r2.left, r3.left)
        dfs(None, r2.right, r3.right)
        return
      elif r1:
        r3.val = r1.val
        dfs(r1.left, None, r3.left)
        dfs(r1.right, None, r3.right)
        return
      else:
        r3 = None
        return

    dfs(root1, root2, root3)

    return root3