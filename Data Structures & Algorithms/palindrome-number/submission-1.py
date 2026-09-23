class Solution:

    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if s[0] == '-':
            return False
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        
        return True

    