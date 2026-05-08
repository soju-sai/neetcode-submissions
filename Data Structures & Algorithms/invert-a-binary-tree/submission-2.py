# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return 
        
        def invert(node):
            if node.right and node.left:
                node.right, node.left = node.left, node.right
                invert(node.right)
                invert(node.left)
            elif node.right:
                node.left = node.right
                node.right = None
                invert(node.left)
            elif node.left:
                node.right = node.left
                node.left = None
                invert(node.right)
        
        invert(root)

        return root

