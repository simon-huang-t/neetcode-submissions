class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = float('inf')
        for i, price in enumerate(prices):
            if price <= buy:
                buy = price
            res = max(res, price - buy)

        return res