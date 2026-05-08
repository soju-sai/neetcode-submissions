class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, cur = [], []
        i, total = 0, 0
        # res = []

        def dfs(i, cur, total):
            # base case
            # print(i, cur, total, res)
            
            if i >= len(nums) or total > target:
                return
            if total == target:
                res.append(cur.copy()) # important
                return

            cur.append(nums[i])
            total += nums[i]
            dfs(i, cur, total)
            cur.pop()
            total -= nums[i]
            i += 1
            dfs(i, cur, total)

        dfs(0, [], 0)
        # print('res:', res)
        return res
