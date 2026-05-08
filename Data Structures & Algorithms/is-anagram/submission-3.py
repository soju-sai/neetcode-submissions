class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for loop each str and save the count of each letter
        # return the bool result of the comparison of counters
        s1 = {}
        s2 = {}
        for l in s:
            s1[l] = s1.get(l, 0) + 1
        for l in t:
            s2[l] = s2.get(l, 0) + 1
        return s1 == s2
