class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        window_start = 0
        max_profit = 0
        for window_end in range(len(prices)):
            buy_price = prices[window_start]
            sell_price = prices[window_end]
            if buy_price >= sell_price:
                window_start = window_end
            else:
                max_profit = max(max_profit, sell_price - buy_price)
        return max_profit

# Time - O(n)
# Space - O(1)
# Brute - two nested loops to check each combination and find max_profit but time is O(n square)


            



        