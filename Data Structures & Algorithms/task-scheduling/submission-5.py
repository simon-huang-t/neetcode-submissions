from collections import deque, Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        1) Count freq of tasks
        2) Add freq in max_heap
        3) Iterate while max_heap or queue
            a) Pop from max_heap
            b) Decrement freq
            c) if freq > 0, add (freq, time_available) to queue
            d) While top of queue is available, add it to max_heap
        4) Return time
        '''
        freq = Counter(tasks)
        max_heap = []
        for _, count in freq.items():
            heapq.heappush_max(max_heap, count)
        queue = deque()
        
        t = 0 #not 1
        while max_heap or queue:
            t += 1 # Here, not at the end
            if max_heap:
                count = heapq.heappop_max(max_heap)
                count -= 1 #indentation
                if count > 0:
                    queue.append((count, t + n))
            while queue and queue[0][1] == t: # ==t
                count, _ = queue.popleft()
                heapq.heappush_max(max_heap, count)
        return t
