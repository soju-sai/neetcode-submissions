# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        self.inDict = { v: i for i, v in enumerate(inorder)}
        self.postIndex = len(postorder) - 1

        def dfs(l, r):
            if l > r:
                return None
            rootVal = postorder[self.postIndex]
            root = TreeNode(rootVal)
            self.postIndex -= 1
            mid = self.inDict[rootVal]
            root.right = dfs(mid + 1 , r)
            root.left = dfs(l, mid - 1)
            return root
        
        return dfs(0, len(inorder)-1)