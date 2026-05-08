class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        max_len = 0
        for c in s:
            if c not in sub:
                sub += c
                max_len = max(len(sub), max_len)
            else:
                sub = sub[sub.index(c) + 1:] + c
                max_len = max(len(sub), max_len)
        return max_len