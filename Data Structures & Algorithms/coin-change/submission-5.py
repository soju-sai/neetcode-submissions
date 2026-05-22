class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return -1 if dp[amount] == (amount + 1) else dp[amount]

    def coinChange_v3(self, coins: List[int], amount: int) -> int:
        res = []
        total = 0

        def dfs(i, cur, total):
            if total == amount:
                res.append(cur.copy())
                return
            if i < 0 or total > amount:
                return

            cur.append(coins[i])
            dfs(i, cur, total + coins[i])
            cur.pop()
            dfs(i-1, cur, total)
        
        dfs(len(coins)-1, [], total)
        result = float('inf')

        for i in range(len(res)):
            result = min(result, len(res[i]))
        
        return -1 if result == float('inf') else result

    def coinChange_v2(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()

        cur = []
        total = 0
        i = len(coins) - 1
        while i >= 0:
            cur.append(coins[i])
            total += coins[i]
            print(total)
            if total == amount:
                return len(cur)
            if total > amount:
                cur.pop()
                total -= coins[i]
                i -= 1
            else:
                continue
            
        return -1

    