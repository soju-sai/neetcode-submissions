class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums = set(nums)
        # print(nums)
        if target in nums:
            return True
        else:
            return False

        # l, r = 0, len(nums) - 1
        # while l < r: # 剛好 l = r的時候會跳出
        #     m = (l + r) // 2
        #     if nums[m] > nums[r]:
        #         l = m + 1
        #     else:
        #         r = m # 一找到比 r 小（或等於r）的 m ，就讓 r = m，
        # # 一直拿mid和最右邊比，找到了大於m的r就表示找到asc的部分
        
        # pivot = l
        # print(pivot)
        # l, r = 0, len(nums) - 1
        # if target >= nums[pivot] and target <= nums[r]:
        #     l = pivot
        # else:
        #     r = pivot - 1

        # while l <= r:
        #     m = (l+r) // 2
        #     if target == nums[m]:
        #         return True
        #     elif target > nums[m]:
        #         l = m + 1
        #     else:
        #         r = m - 1

        # return False
        
        
