class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] == '#' or word[i] != board[r][c]:
                return False
            board[r][c] = '#'
            res = False
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                res |= dfs(nr, nc, i + 1)
            board[r][c] = word[i]
            return res
            

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True

        return False