class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for i in range(len(prices) - 1):
            sell = max(prices[i+1:])
            profit = (sell - prices[i])
            res = max(res, profit)

        return res
        