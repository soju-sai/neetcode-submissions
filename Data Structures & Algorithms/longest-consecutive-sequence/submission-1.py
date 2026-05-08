class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums = list(set(nums))
        nums.sort()
        print(nums)
        current_length = max_length = 1
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                current_length += 1
            else:
                current_length = 1
            if current_length > max_length:
                max_length = current_length
            print(nums[i] - 1, nums[i-1])
            print(current_length, max_length)
        return max_length
