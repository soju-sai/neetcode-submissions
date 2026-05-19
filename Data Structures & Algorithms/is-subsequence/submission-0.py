class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        si = 0
        for j in range(len(t)):
            if s[si] == t[j]:
                si += 1
            if si == len(s):
                return True
        
        return False