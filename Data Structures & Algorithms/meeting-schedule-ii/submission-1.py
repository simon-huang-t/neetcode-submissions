"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for interval in intervals:
            events.append((interval.start, 'S'))
            events.append((interval.end, 'E'))
        events.sort()
        overlapping = 0
        res = 0
        for event_time, event_type in events:
            if event_type == 'S':
                overlapping += 1
            elif event_type == 'E':
                overlapping -= 1
            res = max(res, overlapping)
        return res
            