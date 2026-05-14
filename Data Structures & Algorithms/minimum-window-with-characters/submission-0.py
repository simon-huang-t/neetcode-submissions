class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = 0
        t_count = Counter(t)
        need = len(t_count)
        res_len = float('inf')
        start = 0
        end = 0
        s_count = defaultdict(int)
        l = 0
        for r, c in enumerate(s):
            s_count[c] += 1
            if c in t and s_count[c] == t_count[c]: #Forgot if c in t
                have += 1
                while have == need:
                    if r - l + 1 < res_len:
                        res_len = r - l + 1
                        start, end = l, r
                    s_count[s[l]] -= 1
                    
                    if s[l] in t and s_count[s[l]] < t_count[s[l]] :
                        have -= 1
                    l += 1
        return s[start: end + 1] if res_len != float('inf') else ""