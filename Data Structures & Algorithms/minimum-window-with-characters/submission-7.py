class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        need = len(count_t)
        have = 0
        window_count = defaultdict(int)
        start, end = 0, 0
        resLen = float('inf')
        l = 0
        for r, c in enumerate(s):
            window_count[c] += 1
            if c in count_t and window_count[c] == count_t[c]:
                have += 1
                # if have == need:
                while have == need:
                    if r - l + 1 < resLen:
                        start, end = l, r
                        resLen = r - l + 1
                    left_char = s[l]
                    window_count[left_char] -= 1
                    # l  += 1
                    if left_char in count_t and window_count[left_char] < count_t[left_char]:
                        have -= 1
                    l  += 1
        return s[start: end + 1] if resLen != float('inf') else ''