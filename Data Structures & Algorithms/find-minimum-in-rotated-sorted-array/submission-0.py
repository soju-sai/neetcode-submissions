class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 如果last > first，表示沒有rotate，直接回傳first
        # last < first 就用last開始當起點找
        # last 和 mid 比，last 小的話，從mid右邊繼續找，否則從左邊
        # 直到mid的index不變，回傳那個mid的index
        if len(nums) == 1 or nums[-1] > nums[0]:
            return nums[0]

        min_index = len(nums) - 1
        # min_value = nums[min_index]
        mid = len(nums) // 2
        while True:
            # base case: mid == min_index
            # loop case:
            print(nums[min_index])
            if nums[min_index] < nums[mid]:
                mid = ((mid + 1) + min_index) // 2
            elif nums[min_index] > nums[mid]:
                min_index = mid
                mid = (0 + mid) // 2
            else:
                return nums[min_index]
        

