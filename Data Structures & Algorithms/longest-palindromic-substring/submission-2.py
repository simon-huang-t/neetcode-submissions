class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expandAroundCenter(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return (l + 1, r) #l not valid anymore so we take l+1. r not valid but then we don't need 

        longest = 0
        start = end = 0
        for i in range(n):
            for i0 in (0, 1):
                l, r = expandAroundCenter(i, i+i0)
                if r - l  > longest: # r - l and not r - l + 1
                    longest = r - l 
                    start = l
                    end = r
        return s[start:end]
