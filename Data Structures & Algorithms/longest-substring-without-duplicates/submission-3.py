class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        n = len(s)
        longest = 0
        l = 0
        for r, c in enumerate(s):            
            if c in seen:
                l = max(l, seen[c] + 1)
            seen[c] = r
            longest = max(longest, r - l + 1)
        return longest