class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word)) + '#' + word)
        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        res = []
        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            number = s[i:j]
            start = j + 1
            end = start + int(number)
            res.append(s[start: end])
            i = end
        return res

