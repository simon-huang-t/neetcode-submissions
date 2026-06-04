class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        atlantic, pacific = set(), set()
        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and heights[r][c] <= heights[nr][nc] :
                    dfs(nr, nc, visited)
        for r in range(m):
            dfs(r, 0, pacific)
            dfs(r, n - 1, atlantic)
        for c in range(n):
            dfs(0, c, pacific)
            dfs(m - 1, c, atlantic)
        return list(atlantic & pacific)