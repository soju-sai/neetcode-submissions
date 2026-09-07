class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # base case
        # 1, 2
        if num == 1:
            return True

        l, r = 1, num 
        while l <= r:
            mid = (l + r) // 2
            # root 是每次 num / 2
            # root 的平方 > num, 把 root / 2 繼續找
            sqar = mid * mid
            if sqar > num:
                r = mid - 1
            # root 的平方 <= num, 把 root * 2 繼續找
            elif sqar < num:
                l = mid + 1
            else:
                return True
            
        return False
        