class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev, num = 0, x

        while num:
            rev = (rev * 10) + (num % 10)
            num //= 10
        
        return rev == x

    