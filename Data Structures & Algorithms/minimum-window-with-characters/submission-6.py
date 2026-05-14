from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        have = 0
        need = len(t_count)
        start = end = 0
        l = 0
        res_len = float('inf')
        window_count = defaultdict(int)
        for r, c in enumerate(s):
            window_count[c] += 1
            if c in t_count and window_count[c] == t_count[c]:
                have += 1
                while have == need:
                    if r - l + 1 < res_len:
                        res_len = r - l + 1
                        start, end = l, r
                    char_left = s[l]
                    window_count[char_left] -= 1
                    if char_left in t_count and window_count[char_left] < t_count[char_left]:
                        have -= 1
                    l += 1 
        return s[start:end+1] if res_len != float('inf') else ""