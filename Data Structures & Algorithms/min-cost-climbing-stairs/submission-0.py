class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)

        dp = [0] * len(cost)
        
        for i in range(len(cost) - 1, -1, -1):
            if i == len(cost) - 1 or i == len(cost) - 2:
                dp[i] = cost[i]
            else:
                dp[i] = min(dp[i+1], dp[i+2]) + cost[i]
        
        return min(dp[0], dp[1])

    def minCostClimbingStairs_v1(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        minC = [0] * (len(cost)+1)
        minC[0], minC[1], minC[2] = min(cost), min(cost), min(cost)
        for c in range(3, len(cost)):
            minC[c] = min(cost[c-1], cost[c-2]) + cost[c]
            print(c, minC[c])
        # print(cost[-1])
        # print(minC[len(cost)-1])