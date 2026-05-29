from functools import cache
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        @cache
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = []
        track = []
        
        def dfs(start):
            if start == n:
                res.append(track[:])
                return
            for end in range(start, n): #
                if is_palindrome(start, end):
                    track.append(s[start:end+1])
                    dfs(end+1)
                    track.pop()
        dfs(0)
        return res
