class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        cols = set()
        posDiag = set() #'/'
        negDiag = set() #'\'
        res = []

        def backtrack(row):
            if row == n:
                res.append([''.join(r) for r in board])
                return
            for col in range(n):
                if col in cols or (row - col) in negDiag or (row + col) in posDiag:
                    continue
                board[row][col] = 'Q'
                cols.add(col)
                negDiag.add(row - col)
                posDiag.add(row + col)
                backtrack(row+1)
                board[row][col] = '.'
                cols.remove(col)
                negDiag.remove(row - col)
                posDiag.remove(row + col)
        backtrack(0)
        return res
