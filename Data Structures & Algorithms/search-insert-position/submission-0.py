class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def search(l, r):

            m = (l + r) // 2
            if l > r:
                return l
            if target < nums[m]:
                return search(l, m - 1)
            if target > nums[m]:
                return search(m + 1, r)
            
            return m

        return search(0, len(nums)-1)


        