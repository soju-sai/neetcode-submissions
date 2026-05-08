class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            counter = 0
            b = i
            while b:
                counter += b % 2
                b >>= 1
            output.append(counter)

        return output