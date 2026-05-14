class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            if current_start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], current_end)
            else:
                res.append(intervals[i])
        return res