from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        
        '''
        if len(s) < len(t):
            return ""
        count_t = Counter(t)
        need = len(count_t)
        have = 0
        window_freq = defaultdict(int)
        n = len(s)
        l = 0
        start = end = 0
        resLen = float('inf')
        for r, c in enumerate(s):
            window_freq[c] += 1
            if c in count_t and window_freq[c] == count_t[c]: #
                have += 1
                while have == need:
                    if r - l + 1 < resLen:
                        start, end = l, r
                        resLen = r - l + 1
                    left_char = s[l]
                    window_freq[left_char] -= 1
                    if left_char in count_t and window_freq[left_char] < count_t[left_char]:
                        have -= 1
                    l += 1
        return s[start: end + 1] if resLen != float('inf') else ""
        





