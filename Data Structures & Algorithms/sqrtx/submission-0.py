class Solution:
    def mySqrt(self, x: int) -> int:
        def findRoot(x):
            l, r = 0, x

            while l <= r:
                mid = (l + r) // 2
                sqr = mid * mid
                if sqr > x:
                    r = mid - 1
                elif sqr < x:
                    l = mid + 1
                else:
                    return mid

            return r
        
        return findRoot(x)