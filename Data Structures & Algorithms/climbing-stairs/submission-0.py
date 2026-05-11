class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [None] * (n+1)
        for i in range(1, n+1):
            if i < 3:
                dp[i] = i
            else:
                dp[i] = dp[i-1] + dp[i-2]
                
        return dp[n]