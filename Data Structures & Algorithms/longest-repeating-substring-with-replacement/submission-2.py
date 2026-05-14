class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        longest = 0
        l = 0
        max_frequency = 0
        for r, c in enumerate(s):
            count[c] += 1
            max_frequency = max(max_frequency, count[c])
            while (r - l + 1) - max_frequency > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest