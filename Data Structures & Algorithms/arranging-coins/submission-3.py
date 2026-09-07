class Solution:
    def arrangeCoins(self, n: int) -> int:
        accu = 0
        res = 0
        for i in range(1, n+1):
            accu += i
            if n - accu == 0:
                res = i
                break
            elif n - accu < 0:
                res = i - 1
                break
            
        return res