class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        rob = [0] * len(nums)
        rob[0] = nums[0]
        rob[1] = max(rob[0], nums[1])
        maxAmt = 0

        for i in range(2, len(nums)):
            rob[i] = max(nums[i] + rob[i-2], rob[i-1])
            maxAmt = max(maxAmt, rob[i])
            print(i, rob[i], maxAmt)
            
        return maxAmt

    def rob_v1(self, nums: List[int]) -> int:
        # 如果一定會選跳過一個房子的搶法
        first, second = 0, 1
        max1st, max2nd = 0, 0
        for i in range(len(nums)):
            if ((i - first + 2) % 2 == 0):
                max1st += nums[i]
            if ((i - second + 2) % 2 == 0):
                max2nd += nums[i]
            print(max1st, max2nd)

        return max(max1st, max2nd)