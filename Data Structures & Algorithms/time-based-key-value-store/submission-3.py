import bisect
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # self.time_map[key].append((value, timestamp))
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        index = bisect.bisect_right(self.time_map[key], (timestamp, chr(127)))
        if index == 0:
            return ""
        _, val = self.time_map[key][index - 1]
        return val
        
        
