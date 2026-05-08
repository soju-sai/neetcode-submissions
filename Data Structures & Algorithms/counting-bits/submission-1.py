class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            if i == (offset * 2):
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp

    def countBits_v1(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            counter = 0
            b = i
            while b:
                counter += b % 2
                b >>= 1
            output.append(counter)

        return output