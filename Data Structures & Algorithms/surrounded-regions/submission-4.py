class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        queue = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(m):
            if board[r][0] == 'O':
                queue.append((r, 0))
            if board[r][n - 1] == 'O':
                queue.append((r, n - 1))
        
        for c in range(n):
            if board[0][c] == 'O':
                queue.append((0, c))
            if board[m - 1][c] == 'O':
                queue.append((m - 1, c))
        
        while queue:
            r, c = queue.popleft()
            board[r][c] = 'S'
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                    queue.append((nr, nc))
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'
        