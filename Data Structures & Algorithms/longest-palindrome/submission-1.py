class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        counts = Counter(s)

        length, odds = 0, 0
        print(counts)
        for v in counts.values():
            if v % 2 == 1:
                odds += 1
                length += v - 1
            else:
                length += v

        if odds > 0:
            length += 1

        return length