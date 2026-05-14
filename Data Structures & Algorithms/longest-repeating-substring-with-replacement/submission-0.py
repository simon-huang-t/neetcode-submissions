class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        count = defaultdict(int)
        for r, c in enumerate(s):
            count[c] += 1
            max_frequency = max(count.values())
            while (r - l + 1) - max_frequency > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest