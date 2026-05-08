# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor_Recursive(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Recursive
        # root是none的話，回傳none
        # p, q同時小於root的話，找左邊的樹
        # p, q同時大於root的話，找右邊的樹
        # 不同時小於或大於，就是分歧點，在左右或是在node上
        if not root:
            return None
        
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Iteration

        # root是none的話，回傳none
        # p, q同時小於root的話，找左邊的樹
        # p, q同時大於root的話，找右邊的樹
        # 不同時小於或大於，就是分歧點，在左右或是在node上
        
        node = root

        while node:
            print(p.val, q.val, node.val)
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node
        