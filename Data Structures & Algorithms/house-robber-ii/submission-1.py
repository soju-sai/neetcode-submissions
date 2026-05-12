class Solution:
    def rob(self, nums: List[int]) -> int:
        def rubber(nums):
            maxAmt = [-1] * len(nums)
            maxAmt[0] = nums[0]
            if len(nums) == 1:
                return maxAmt[0]
            maxAmt[1] = max(maxAmt[0], nums[1])
            if len(nums) == 2:
                return maxAmt[1]

            for i in range(2, len(nums)):
                maxAmt[i] = max(nums[i] + maxAmt[i-2], maxAmt[i-1])

            return maxAmt[len(nums)-1]

        if len(nums) == 1:
                return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(rubber(nums[0:len(nums)-1]), rubber(nums[1:len(nums)]))