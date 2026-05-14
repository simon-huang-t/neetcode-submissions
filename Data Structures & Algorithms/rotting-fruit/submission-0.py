class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minutes = 0
        fruits = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    fruits += 1
                if grid[r][c] == 1:
                    fruits += 1
                
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                fruits -= 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 2
            if queue:
                minutes += 1
        return minutes if fruits == 0 else -1
        