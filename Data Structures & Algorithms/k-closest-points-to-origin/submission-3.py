class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        def euclidean_distance(x, y):
            return x**2 + y**2
        
        for x, y in points:
            dist = euclidean_distance(x, y)
            heapq.heappush_max(heap, (dist, x, y))
            if len(heap) > k:
                heapq.heappop_max(heap)
        return [[x, y] for _, x, y in heap]