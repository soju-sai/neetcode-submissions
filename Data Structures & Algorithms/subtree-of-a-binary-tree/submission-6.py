# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
      def isSub(r, s):
        if not r and not s:
          return True
        if r and s and r.val == s.val:
          return isSub(r.left, s.left) and isSub(r.right, s.right)
        else:
          return False
          
      def dfs(r, s):
        if not r or not s:
          return False
        if isSub(r, s):
          return True
        
        return dfs(r.left, s) or dfs(r.right, s)
        
      return dfs(root, subRoot)

    def isSubtree_v1(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 用recursive DFS traversal
        if not root:
            return False
        if not subRoot:
            return False
        
        # 用same tree的方式比較
        if self.isSame(root, subRoot):
            return True
            
        # 沒找到就繼續找Root的其他部分
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, r, s):
        # 如果r和s都是None就是true
        # 如果r和s都有值且val相同，重複確認left和right
        # 其他情況return False
        if not r and not s:
            return True
        if r and s and r.val == s.val:
            return self.isSame(r.left, s.left) and self.isSame(r.right, s.right)
        else:
            return False
        
        
