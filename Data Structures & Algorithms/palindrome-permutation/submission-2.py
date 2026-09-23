class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        from collections import Counter
        counts = Counter(s)
        oddCounts = sum(val % 2 for val in counts.values())
        
        return oddCounts <= 1