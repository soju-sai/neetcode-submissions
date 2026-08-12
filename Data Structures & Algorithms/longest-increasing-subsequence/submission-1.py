class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * (n+1) for _ in range(n)]

        # i is the current index, j is the last included index
        def dfs(i, j):
          # base case: the current index is out of bound
          if i == len(nums):
            # no adding of length
            return 0
          if memo[i][j+1] != -1:
            return memo[i][j+1]

          # skip the current index
          LIS = dfs(i + 1, j)

          # include i when current greater than last, or there is no last
          if j == -1 or nums[i] > nums[j]:
            # include meaning the length increase one
            LIS = max(LIS, 1 + dfs(i + 1, i))

          memo[i][j+1] = LIS

          return LIS

        return dfs(0, -1)