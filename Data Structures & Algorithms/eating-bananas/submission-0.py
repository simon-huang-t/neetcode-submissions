class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        l, r = 1, max(piles)
        def can_eat(k):
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            return time <= h


        
        while l < r:
            mid = (l + r) // 2
            if can_eat(mid):
                r = mid
            else:
                l = mid + 1
        return l