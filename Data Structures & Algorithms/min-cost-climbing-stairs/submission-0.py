from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        @cache
        def dp(i):
            if i == n:
                return 0
            if i > n:
                return float('inf')
            
            res = cost[i] + min(dp(i+1), dp(i+2))
            return res

        return min(dp(0), dp(1))

        