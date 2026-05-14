class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = 0
        t_count = Counter(t)
        need = len(t_count)
        if len(s) < len(t):
            return ""
        res = [0, 0]
        resLen = float('inf')
        l = 0
        window_count = defaultdict(int)
        for r, c in enumerate(s):
            window_count[c] += 1
            if c in t_count and window_count[c] == t_count[c]:
                have += 1
                while have == need:
                    if resLen > (r - l + 1):
                        resLen = r - l + 1
                        res = [l, r]
                    charLeft = s[l]
                    window_count[charLeft] -= 1
                    if charLeft in t_count and window_count[charLeft] < t_count[charLeft]:
                        have -= 1 
                    l += 1
        start, end = res
        return s[start:end+1] if resLen != float('inf') else ""