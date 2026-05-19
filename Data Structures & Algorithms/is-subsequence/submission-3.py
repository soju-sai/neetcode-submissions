class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        i, j = 0, 0
        while j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            if i == len(s):
                return True
            while j < len(t) and t[j] != s[i]:
                j += 1
                if j == len(t):
                    return False
            # j += 1
        
        return False