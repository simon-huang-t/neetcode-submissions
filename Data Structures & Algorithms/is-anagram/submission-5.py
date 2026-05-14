class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26


        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for val in count:
            if val != 0:
                return False
        return True
        



        
        # s_count = defaultdict(int)
        # t_count = defaultdict(int)
        # for c in s:
        #     s_count[c] += 1
        # for c in t:
        #     t_count[c] += 1
        # return s_count == t_count
            