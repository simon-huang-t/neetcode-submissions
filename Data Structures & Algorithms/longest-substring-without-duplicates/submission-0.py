class Solution:
    # abcbcad
    #     r
    # l
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        n = len(s)
        longest = 0
        for r, c in enumerate(s):
            if c in seen and l <= seen[c]:
                l = seen[c] + 1
            seen[c] = r
            longest = max(longest, r - l + 1)
        return longest