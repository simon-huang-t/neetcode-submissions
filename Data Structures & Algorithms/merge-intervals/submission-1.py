class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for ns, ne in intervals[1:]:
            s, e = res[-1]
            if e >= ns: #overlapping --> merge
                res[-1][1] = max(e, ne)
            else:
                res.append([ns, ne])
        return res