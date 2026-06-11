class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def can_eat(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            return hours <= h
            
        ans = r

        while l <= r:
            mid = (l + r) // 2

            if can_eat(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans