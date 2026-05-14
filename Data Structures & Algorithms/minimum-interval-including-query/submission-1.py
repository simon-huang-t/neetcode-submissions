class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        n = len(intervals)
        ans = [-1] * len(queries)
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        heap = []
        idx = 0 #interval idx
        for q, i in sorted_queries:
            while idx < n and intervals[idx][0] <= q:
                l, r = intervals[idx]
                size = r - l + 1
                heapq.heappush(heap, (size, r))
                idx += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                ans[i] = heap[0][0]
        return ans