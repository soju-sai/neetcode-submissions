class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_profit = 0
        max_profit = 0
        min_index = 0

        for i in range(1, len(prices)):
            if (prices[i] - prices[min_index]) > current_profit:
                current_profit = prices[i] - prices[min_index]
            if current_profit > max_profit:
                max_profit = current_profit
            if prices[i] < prices[min_index]:
                min_index = i
                current_profit = 0
            print('i', prices[i])
            print('current_profit', current_profit)
            print('max_profit', max_profit)
        
        return max_profit