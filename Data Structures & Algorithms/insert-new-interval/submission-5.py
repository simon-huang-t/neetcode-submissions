class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, interval in enumerate(intervals):
            start, end = interval
            newStart, newEnd = newInterval
            if newEnd < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif end < newStart:
                res.append(interval)
            else:
                newInterval[0] = min(start, newStart)
                newInterval[1] = max(end, newEnd)
        res.append(newInterval)
        return res