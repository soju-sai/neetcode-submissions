class Solution:
    def tribonacci(self, n: int) -> int:
        trib = [None] * (n+1)
        
        def dfs(n):
            if n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            elif trib[n]:
                return trib[n]

            trib[n] = dfs(n-3) + dfs(n-2) + dfs(n-1)
            return trib[n]
        
        return dfs(n)