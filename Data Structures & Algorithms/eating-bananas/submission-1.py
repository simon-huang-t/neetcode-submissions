from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(K):
            hours = 0
            for p in piles:
                hours += math.ceil(p / K)
            return hours <= h

        # l, r = max(piles), sum(piles)
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if can_eat(mid):
                r = mid
            else:
                l = mid + 1
        return l