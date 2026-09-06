class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(l, r):
            mid = (l + r) // 2
            print(mid, nums[mid])
            if l > r:
                return - 1
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                return bs(l, mid - 1)
            if target > nums[mid]:
                return bs(mid + 1, r)

        return bs(0, len(nums) - 1)