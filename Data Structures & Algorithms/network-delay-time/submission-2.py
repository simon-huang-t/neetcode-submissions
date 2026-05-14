class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, t in times:
            edges[u].append((v, t)) #node, weight
        heap = [(0, k)] #weight, node
        visited = set()
        t = 0
        while heap:
            w1, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            t = max(t, w1)
            for v, w in edges[u]:
                if v not in visited:
                    heapq.heappush(heap, (w + w1, v))

        return t if len(visited) == n else -1