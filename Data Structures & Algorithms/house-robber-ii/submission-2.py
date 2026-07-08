class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def maxRobber(moneyAmounts):
            if len(moneyAmounts) == 1:
                return moneyAmounts[0]
            dp = [-1] * len(moneyAmounts)
            dp[0] = moneyAmounts[0]
            dp[1] = max(moneyAmounts[0], moneyAmounts[1])
            if len(moneyAmounts) == 2:
                return dp[1]
            for i in range(2, len(moneyAmounts)):
                dp[i] = max(dp[i-1], dp[i-2] + moneyAmounts[i])
            
            return dp[len(moneyAmounts)-1]

        return max(maxRobber(nums[:len(nums)-1]), maxRobber(nums[1:len(nums)]))