class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visited:
                    dfs(nr, nc, visited)

        for c in range(n):
            dfs(0, c, pacific)
            dfs(m - 1, c, atlantic)
        
        for r in range(m):
            dfs(r, 0, pacific)
            dfs(r, n - 1, atlantic)

        

        return list(pacific & atlantic)