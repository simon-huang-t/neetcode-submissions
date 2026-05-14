class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set({(0, 0)})
        heap = [(grid[0][0], 0, 0)] # (time, r, c)
        n = len(grid)
        target = (n - 1, n - 1)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while heap:
            t, r, c = heapq.heappop(heap)
            if (r, c) == target:
                return t
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    new_t = max(t, grid[nr][nc])
                    heapq.heappush(heap, (new_t, nr, nc))
                    visited.add((nr, nc))
        return t
