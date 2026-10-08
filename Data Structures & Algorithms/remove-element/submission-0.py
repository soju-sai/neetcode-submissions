class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for n in nums.copy():
            if n == val:
                nums.remove(n)
                
        return len(nums)