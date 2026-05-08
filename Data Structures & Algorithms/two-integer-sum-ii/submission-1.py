class Solution:
    def twoSum_hp(self, numbers: List[int], target: int) -> List[int]:
        # hash map的key存需要的餘值，value存那個key的index，藉由key可以快速判斷是否存在
        hp = defaultdict(int)
        for i in range(len(numbers)):
            if hp[numbers[i]]:
                return [hp[numbers[i]], i + 1]
            hp[target - numbers[i]] = i + 1
        return []
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers：一個從左邊，一個從右邊
        # loop:
        # base case: 找到左右和==target，就回傳各自的index+1
        # 左右和不等於target就繼續找，最後都沒有就是回傳[]
        # 總和小於target的話，讓左邊index加1
        # 總和大於target的話，讓右邊index減1
        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            if numbers[l] + numbers[r] < target:
                l+=1
            elif numbers[l] + numbers[r] > target:
                r-=1
        return []