class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        remove = 0
        intervals.sort(key = lambda x: x[1])
        e = intervals[0][1]
        for ns, ne in intervals[1:]:
            if e > ns:
                remove += 1
            else:
                e = ne
        return remove