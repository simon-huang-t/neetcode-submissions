class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_frequency = 0
        seen = defaultdict(int)
        l = 0
        longest = 0
        for r, c in enumerate(s):
            seen[c] += 1
            if seen[c] > max_frequency:
                max_frequency = seen[c]
            while (r - l + 1) - max_frequency > k:
                seen[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest