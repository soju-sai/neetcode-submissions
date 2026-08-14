class Solution:
    def countBits(self, n: int) -> List[int]:
        memo = [0] * (n+1)
        
        for i in range(n+1):
            count = 0
            tmp = i

            while tmp > 0:
                if memo[tmp] > 0:
                    memo[i] = memo[tmp] + count
                    break
                if tmp & 1 == 1:
                    count += 1
                tmp = tmp >> 1
                if tmp == 0:
                    memo[i] = count

        return memo