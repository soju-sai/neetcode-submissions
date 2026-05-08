class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 用一個字典存[之前的值: index]
        # 確認字典的記錄裡有：目前的值和之前的值相加 == target 就可以回傳index了
        addends = {}
        for i, v in enumerate(nums):
            if (target - v) in addends:
                return [addends.get(target - v), i]
            else:
                addends[v] = i

        