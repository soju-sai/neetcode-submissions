class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0
        n = len(s)
        for i in range(n):
            l, r = i, i
            while l > -1 and r < n and s[l] == s[r]:
                if len(s[l:r+1]) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l > -1 and r < n and s[l] == s[r]:
                if len(s[l:r+1]) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
        return res
