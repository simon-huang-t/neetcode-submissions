from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        @cache
        def _count(i, target):
            if target == 0:
                return 1
            if i >= len(coins):
                return 0
            count = 0
            if target - coins[i] >= 0:
                count = _count(i + 1, target)
                count += _count(i, target - coins[i])
            return count
        
        return _count(0, amount)
