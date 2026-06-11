class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        l, r = 0, len(values) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            candidate_value, candidate_timestamp = values[mid]
            if candidate_timestamp <= timestamp:
                res = candidate_value
                l = mid + 1
            else:
                r = mid - 1
        return res
        
