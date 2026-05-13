class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res

    def longestPalindrome_v1(self, s: str) -> str:
        if len(s) == 1:
            return s

        if len(s) % 2 == 0:
            l, r = int((len(s) / 2) - 1) , int(len(s) / 2)
        else:
            l, r = int((len(s) / 2) - 1) , int(len(s) / 2 + 1)

        last = len(s) - 1

        

        # print(s[l], s[r])
        def dfs(l, r, long):
            if l < 0 or r > last or s[l] != s[r]:
                return long
            if s[l] == s[r]:
                long = s[l:r+1]
                l -= 1
                r += 1
                dfs(l, r, long)
        
        return s