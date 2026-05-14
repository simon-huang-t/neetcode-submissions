class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        heapq.heapify_max(stones)
        while len(stones) > 1:
            heaviest = heapq.heappop_max(stones)
            second_heaviest = heapq.heappop_max(stones)
            if heaviest != second_heaviest:
                heapq.heappush_max(stones, heaviest - second_heaviest)
        return stones[0] if stones else 0
