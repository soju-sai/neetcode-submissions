class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 1:
        #     return 1
        if n <= 2:
            return n

        dp = [0] * (n+1)
        # dp[0] = 0
        dp[1], dp[2] = 1, 2
        # print(dp)
        for k in range(3, n+1):
            dp[k] = dp[k-1] + dp[k-2]

        return dp[n]