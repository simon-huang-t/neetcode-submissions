from collections import deque, Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        # max_heap = []
        # for count in freq.values():
        #     heapq.heappush_max(max_heap, count)
        max_heap = list(freq.values())
        heapq.heapify_max(max_heap)
        queue = deque()
        t = 0
        while max_heap or queue:
            t += 1
            if max_heap: # Forgot this
                count = heapq.heappop_max(max_heap)
                count -= 1
                if count > 0:
                    queue.append((count, t + n))
            while queue and queue[0][1] == t:
                count, _ = queue.popleft() # forgot to unpack _
                heapq.heappush_max(max_heap, count)
            # pop from max_heap
            # decrement count
            # push to queue (count, available_time) if count > 0
            # while top of the queue has a time == current_time
            #   count = queue.popleft()
            #   heapq.heappush_max(heap, count)
        return t