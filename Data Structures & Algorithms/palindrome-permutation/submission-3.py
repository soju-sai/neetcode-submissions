class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        remain = set()
        for c in s:
            if c in remain:
                remain.remove(c)
            else:
                remain.add(c)

        return len(remain) <= 1