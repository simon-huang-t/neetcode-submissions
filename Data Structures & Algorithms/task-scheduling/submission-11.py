from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        max_heap = []
        queue = deque()
        freq = Counter(tasks)
        for value in freq.values():
            heapq.heappush_max(max_heap, value)
        while max_heap or queue:
            time += 1
            if max_heap:
                count = heapq.heappop_max(max_heap)
                count -= 1
                if count > 0:
                    queue.append((count, time + n))
            if queue and queue[0][1] == time:
                count, _ = queue.popleft()
                heapq.heappush_max(max_heap, count)
        return time