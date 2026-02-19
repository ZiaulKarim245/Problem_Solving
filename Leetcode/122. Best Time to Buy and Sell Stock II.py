class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit, n = 0, len(prices)
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit