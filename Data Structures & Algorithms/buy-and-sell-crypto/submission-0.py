class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j, n = 0, 1, len(prices)
        max_profit = 0
        while j < n:
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
            
            if prices[j] < prices[i]: i = j
            j += 1
        return max_profit
