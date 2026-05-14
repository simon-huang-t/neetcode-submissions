class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = [0] * 26
        t_count = [0] * 26

        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
            t_count[ord(t[i]) - ord('a')] += 1
        return s_count == t_count
        



        
        # s_count = defaultdict(int)
        # t_count = defaultdict(int)
        # for c in s:
        #     s_count[c] += 1
        # for c in t:
        #     t_count[c] += 1
        # return s_count == t_count
            