class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = 2
        ans = []
        while n > 0:
            for i in nums:
                ans.append(i)
            n -= 1
        
        print(ans)
        return ans