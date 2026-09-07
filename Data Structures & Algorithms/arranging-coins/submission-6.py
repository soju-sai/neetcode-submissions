class Solution:
    def arrangeCoins(self, n: int) -> int:
        def arrange(n):
            if n <= 3:
                return n if n == 1 else n - 1

            l, r = 1, n
            res = 0

            while l <= r:
                mid = (l + r) // 2
                accu = mid * (mid + 1) / 2
                if accu <= n:
                    l = mid + 1
                    # res = max(mid, res)
                if accu > n:
                    r = mid - 1

            return l - 1

        def brute(n):
            accu = 0
            res = 0
            for i in range(1, n+1):
                accu += i
                if n - accu == 0:
                    res = i
                    break
                elif n - accu < 0:
                    res = i - 1
                    break
            return res
            
        return arrange(n)