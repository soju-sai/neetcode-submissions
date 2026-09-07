class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        def findTargetStart():
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r) // 2
                # print(l, r, nums[mid])
                if target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        def checkMaj(start, expect):
            count = 0
            for i in range(start, len(nums)):
                if nums[i] == target:
                    count += 1
                
            return count > expect

        start = findTargetStart()

        return checkMaj(start, len(nums) / 2)