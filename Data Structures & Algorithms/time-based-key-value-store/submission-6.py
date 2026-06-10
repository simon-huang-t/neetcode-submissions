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
        values = self.time_map[key]
        l, r = 0, len(values) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1
        return res


        
