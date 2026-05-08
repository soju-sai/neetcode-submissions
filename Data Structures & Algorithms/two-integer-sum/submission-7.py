class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_copy = nums.copy()
        for n in range(len(nums)):
            poped = nums_copy.pop(0)
            rest = target - poped
            if rest in nums_copy:
                return [n, nums_copy.index(rest) + n +1]
        return []