from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        freq = Counter(tasks)
        max_heap = []
        for count in freq.values():
            heapq.heappush_max(max_heap, count)
        queue = deque()
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