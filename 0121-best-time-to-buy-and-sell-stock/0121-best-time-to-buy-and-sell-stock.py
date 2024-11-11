class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        window_start = 0
        max_profit = 0 
        for window_end in range(len(prices)):
            if prices[window_start] < prices[window_end]:
                max_profit = max(max_profit, prices[window_end] - prices[window_start])
            else:
                window_start = window_end
        return max_profit
            



        