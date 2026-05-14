class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def expandAroundCenter(l, r):
            count = 0
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        for i in range(n):
            for j in (0, 1):
                count += expandAroundCenter(i, i+j)
        return count