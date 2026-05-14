from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache(None)
        def _uniquePaths(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            return _uniquePaths(i + 1, j) + _uniquePaths(i, j + 1)
        return _uniquePaths(0, 0)