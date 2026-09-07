# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        res = -1
        
        while res != 0:
            pick = (low + high) // 2
            res = guess(pick)
            
            if res > 0:
                low = pick + 1
            else:
                high = pick -1
            
        return pick