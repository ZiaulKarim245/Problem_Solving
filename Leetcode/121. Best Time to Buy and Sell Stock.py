class Solution:
    def maxProfit(self,prices):
        profit = 0
        buy = prices[0]
        for a in prices[1:]:
            buy = min(a,buy)
            profit = max(profit,a-buy)
        return profit

prices = list(map(int,input().split()))
obj = Solution()
print(obj.maxProfit(prices))