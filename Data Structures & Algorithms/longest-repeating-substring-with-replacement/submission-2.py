class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # capitalLetter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # count = {letter: 0 for letter in capitalLetter}
        # maxF = 0
        l, r = 0, 0
        count = {}
        res = 0

        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            # for c in count:
            #     if count.get(theLetter, 0) > maxF:
            #         maxF = count.get(theLetter, 0)
            
            # (r - l + 1) is window size, is it valid window?
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
        
            res = max(res, r - l + 1)
            r += 1

        return res