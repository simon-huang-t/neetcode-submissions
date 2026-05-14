class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start = end = 0
        res = []
        last_seen = {}
        for i, c in enumerate(s):
            last_seen[c] = i
        for i, c in enumerate(s):
            end = max(end, last_seen[c])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res