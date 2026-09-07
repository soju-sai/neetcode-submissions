class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        # l,  r = 0, len(arr) - 1
        diff = int((arr[len(arr)-1] - arr[0]) / len(arr))
        # print(diff)
        for i in range(len(arr)-1):
            if arr[i + 1] - arr[i] != diff:
                return arr[i] + diff

        return arr[0]