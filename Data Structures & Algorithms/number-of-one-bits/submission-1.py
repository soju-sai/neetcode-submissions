class Solution:
    def hammingWeight_v2(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res

    def hammingWeight(self, n: int) -> int:
        counter = 0
        for i in range(32):
            if n & (1 << i):
                counter += 1
        
        return counter
