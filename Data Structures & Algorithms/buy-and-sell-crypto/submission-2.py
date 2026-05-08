class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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