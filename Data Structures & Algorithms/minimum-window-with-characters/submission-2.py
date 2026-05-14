class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = 0
        t_count = Counter(t)
        need = len(t_count)
        res_len = float('inf')
        start, end = 0, 0
        s_count = defaultdict(int)
        l = 0
        for r, c in enumerate(s):
            s_count[c] += 1
            if c in t_count and s_count[c] == t_count[c]:
                have += 1
                while have == need: # The while!
                    if res_len > r - l + 1:
                        res_len = r - l + 1
                        start, end = l, r
                    char_left = s[l]
                    s_count[char_left] -= 1
                    if char_left in t_count and s_count[char_left] < t_count[char_left]:
                        have -= 1
                    l += 1
        return s[start: end + 1] if res_len != float('inf') else ""

