class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pq = [(grid[0][0], 0, 0)] #(time, r, c)
        visited = set({(0, 0)}) #(r, c)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        target = (n - 1, n - 1)
        while pq:
            t, r, c = heapq.heappop(pq)
            if (r, c) == target:
                return t
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    new_t = max(t, grid[nr][nc])
                    heapq.heappush(pq, (new_t, nr, nc))
                    visited.add((nr, nc))

