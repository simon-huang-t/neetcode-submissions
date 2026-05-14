class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row_has_zeros = False
        first_column_has_zeros = False
        m, n = len(matrix), len(matrix[0])
        for c in range(n):
            if matrix[0][c] == 0:
                first_row_has_zeros = True
                break
        for r in range(m):
            if matrix[r][0] == 0:
                first_column_has_zeros = True
                break
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        if first_row_has_zeros:
            for c in range(n):
                matrix[0][c] = 0

        if first_column_has_zeros:
            for r in range(m):
                matrix[r][0] = 0

