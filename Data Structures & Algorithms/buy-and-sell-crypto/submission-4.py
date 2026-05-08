class Solution:
    def maxProfit_v1(self, prices: List[int]) -> int:
        current_profit = 0
        max_profit = 0
        buy_index = min_index = max_index = 0

        for i in range(1, len(prices)):
            if (prices[i] - prices[buy_index]) > current_profit:
                current_profit = prices[i] - prices[buy_index]
            if current_profit > max_profit:
                max_profit = current_profit
                min_index = buy_index
                max_index = i
            if prices[i] < prices[buy_index]:
                buy_index = i
                current_profit = 0
            
        print('min_index:', min_index, 'max_index:', max_index)
        
        return max_profit

    # two_pointers
    def maxProfit_two_pointers(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        
        return max_profit

    # dynamic programming
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]

        for sell in prices:
            max_profit = max(sell - min_buy, max_profit)
            min_buy = min(sell, min_buy)

        return max_profit

