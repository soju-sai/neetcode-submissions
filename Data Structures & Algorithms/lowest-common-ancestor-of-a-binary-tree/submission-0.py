# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        common = None

        def dfs(root):
            nonlocal common
            if not root or common:
                return [False, False]

            left = dfs(root.left)
            right = dfs(root.right)
            foundP = left[0] or right[0] or (root.val == p.val)
            foundQ = left[1] or right[1] or (root.val == q.val)

            if foundP and foundQ and (not common):
                common = root

            return [foundP, foundQ]

        dfs(root)
        return common

        # -------
        # common = None
        # # found = [None, None] # [p, q]

        # def dfs(root):
        #     nonlocal common
        #     if not root:
        #         return [None, None]

        #     found = [None, None] # [p, q]

        #     if root.val == p.val:
        #         found[0] = root.val
        #         # return found
        #     if root.val == q.val:
        #         found[1] = root.val
        #         # return found

        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     print(found, left, right)

        #     if left[0] or left[1] or right[0] or right[1]:
        #         if root.val == p.val or root.val == q.val or (left[0] and right[1]) or (left[1] and right[0]):
        #             common = root.val

        #     return found

        # dfs(root)
        # return common

        # -------

        # common = None
        # found = [None, None] # [p, q]

        # def dfs(root):
        #     nonlocal found, common
        #     if not root:
        #         return None

        #     if root.val == p.val:
        #         found[0] = root.val
        #     if root.val == q.val:
        #         found[1] = root.val

        #     left = dfs(root.left)
        #     right = dfs(root.right)

        #     if found[0] and found[1]:
        #         common = root
            
        #     return found


        # dfs(root)
        # return common

        # -------

        # common = None

        # def dfs(root):
        #     nonlocal common
        #     if not root:
        #         return None
        #     found = None

        #     if root.val == p.val or root.val == q.val:
        #         found = root.val
        #         return root.val

        #     left = dfs(root.left)
        #     right = dfs(root.right)
            
        #     if (left and right) or (left and found) or (right and found):
        #         common = root

        # dfs(root)
        # return common

