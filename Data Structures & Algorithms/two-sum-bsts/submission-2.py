# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        # 先跑一次 roo1 把 root1 的結果存在 hashmap
        # 再跑 root2 確認每個 node.val 有沒有存在 hashmap 的 key 裡
        memo = defaultdict()
        
        def createMemo(r1):
            if not r1:
                return None
            
            memo[target - r1.val] = True
            createMemo(r1.left)
            createMemo(r1.right)
            
            return None

        def dfs(r2):
            if not r2:
                return False
            
            if r2.val in memo:
                return True

            # if target - r2.val > r2.val:
            #     res = dfs(r2.right)
            # elif target - r2.val < r2.val:
            #     res = dfs(r2.left)
            # else:
            #     return True
            # if target - r2.val == r2.val:
            left = dfs(r2.left)
            right = dfs(r2.right)
            if left or right:
                return True
            
            return False

        createMemo(root1)

        return dfs(root2)


        # memo = defaultdict()
        # found = False

        # def dfs(r1, r2):
        #     nonlocal found
        #     if not r2:
        #         return False
        #     if found:
        #         return True

        #     need = target - r1.val
        #     if need == r2.val:
        #         memo[need] = True
        #         found = True
        #         return True
            
        #     if need > r2.val:
        #         res = dfs(r1, r2.right)
        #     elif need < r2.val:
        #         res = dfs(r1, r2.left)

        #     if res:
        #         return True
            
        #     dfs(r1.left, )


        # return dfs(root1, root2)