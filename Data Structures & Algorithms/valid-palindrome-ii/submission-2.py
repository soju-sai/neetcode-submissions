class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        
        def validP(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True    

        while l < r:
            if s[l] != s[r]:
                return validP(l+1, r) or validP(l, r-1)
            l, r = l + 1, r - 1
        
        return True
            