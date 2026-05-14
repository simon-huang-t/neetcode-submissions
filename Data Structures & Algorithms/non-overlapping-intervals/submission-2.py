class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        remove = 0
        intervals.sort(key = lambda x: x[1])
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if prevEnd > start:
                remove += 1
            else:
                prevEnd = end
        return remove