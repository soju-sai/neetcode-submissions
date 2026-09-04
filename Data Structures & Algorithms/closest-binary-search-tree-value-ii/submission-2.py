# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        memo = []
        def dfs(root):
            nonlocal k
            if not root:
                return

            diff = abs(target - root.val)
            # memo.append({diff: root.val})
            memo.append((diff, root.val))

            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        # memo.sort(key=lambda x: next(iter(x)))
        # res = [next(iter(d.values())) for d in memo[:k]]
        memo.sort()
        res = [v for i, v in memo[:k]]

        return res
