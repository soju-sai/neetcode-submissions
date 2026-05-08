class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls, lt = {}, {}
        for i in s:
            ls[i] = ls.get(i, 0) + 1
        for i in t:
            lt[i] = lt.get(i, 0) + 1
        if (ls == lt):
            return True
        return False