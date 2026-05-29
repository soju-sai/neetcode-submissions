class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        note = {len(s): True}

        def dfs(i):
            if i in note:
                print("i", i, note[i])
                return note[i]
            for w in wordDict:
                if ((i + len(w) <= len(s)) and
                    s[i:i+len(w)] == w):
                    # 這裡錯：要看dfs最後的結果一起紀錄到note[i]，中途就記錄True，後續有False就會誤差
                    # note[i] = True
                    # return dfs(i + len(w))
                    if dfs(i + len(w)):
                        note[i] = True
                        return True
            note[i] = False
            print("i", i, note[i])
            return False

        return dfs(0)

    def wordBreak_bottom_up(self, s: str, wordDict: List[str]) -> bool:
        # wordmap = {wordDict[i]: False for i in range(len(wordDict))}
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]
        