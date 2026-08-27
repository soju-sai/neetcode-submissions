# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        return root
        
        # def insertBST(node, target):
        #     if not node:
        #         return TreeNode(target)

        #     if target < node.val:
        #         node.left = insertBST(node.left, target)
        #     if target > node.val:
        #         node.right = insertBST(node.right, target)

        #     return node
        
        # return insertBST(root, val)