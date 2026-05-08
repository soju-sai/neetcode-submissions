class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and target != nums[0]:
            return -1
        if target == nums[0]:
            return 0

        # 用兩次binary search
        # 先找pivot，最小數字的位置。
        #   跑binary search，最後while會停止在left會跟right相會的位置，也就是pivot
        # 再從pivot的左邊還是右邊找target
        l, r= 0, len(nums)-1
        
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l
        l, r= 0, len(nums)-1
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1
        
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            # if m == l:
            #     return -1
            if target > nums[l]:
                l = m + 1
            else:
                r = m - 1
        return -1
        
        # # target < 1st 的話，從 right 開始找
        # if target < nums[0]:
        #     l, r = math.ceil(len(nums) / 2), len(nums)-1
        # else:
        #     l, r = 0, math.ceil(len(nums) / 2)

        # while l < r:
        #     print("l, r:", l, r)
        #     if target in [nums[l], nums[r]]:
        #         res = l if target == nums[l] else r
        #         return res
        #     if target < nums[r]:
        #         l = (l + r) // 2
        #     else:
        #         r = (l + r) // 2
        # return -1
