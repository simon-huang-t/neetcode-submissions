class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.mat = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                self.mat[r][c] = matrix[r-1][c-1] + self.mat[r][c - 1] + self.mat[r - 1][c] - self.mat[r - 1][c - 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.mat[row2+1][col2+1] - self.mat[row1][col2+1] - self.mat[row2+1][col1] + self.mat[row1][col1]
        # return self.mat[row2][col2] - self.mat[row1 - 1][col2] - self.mat[row2][col1 - 1] + self.mat[row1 - 1][col1  - 1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)