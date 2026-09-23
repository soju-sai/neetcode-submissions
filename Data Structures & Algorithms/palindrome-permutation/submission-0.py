class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = {}
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        if (len(s) % 2) == 0:
            for i, v in count.items():
                if v % 2 != 0:
                    return False
        else:
            permu = 1
            for i, v in count.items():
                if v % 2 != 0:
                    if permu < 1:
                        return False
                    permu -= 1
            
        return True
            