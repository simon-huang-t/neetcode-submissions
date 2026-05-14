from functools import cache
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        @cache
        def isPalindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        n = len(s)

        def backtrack(i, track):
            if i == n:
                res.append(track[:])
                return
            for j in range(i, n):
                if isPalindrome(i, j):
                    track.append(s[i:j+1])
                    backtrack(j + 1, track)
                    track.pop()


        backtrack(0, [])
        return res
        