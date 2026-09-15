class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return True
            
            # 先確認哪一半是遞增的，最麻煩的case是剛好重複，那就讓左邊+1
            print(l, r, m)
            # 表示左半邊是排好序的遞增，可以從左半邊找
            if nums[l] < nums[m]:
                # 看 target 在不在這段，因為進來的條件不包含m，所以也不能包含m
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else: # 既然 target 不在這段就跳過
                    l = m + 1
            # 表示右半邊有遞增
            elif nums[l] > nums[m]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else: # 既然 target 不在這段就跳過
                    r = m - 1
            # 表示 l = m
            else:
                l = l + 1
            
        return False