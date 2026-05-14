class MedianFinder:

    def __init__(self):
        self.low = [] #max_heap
        self.high = [] #min_heap

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.low, num)
        heapq.heappush(self.high, heapq.heappop_max(self.low))
        if len(self.low) != len(self.high):
            heapq.heappush_max(self.low, heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) != len(self.high):
            return self.low[0]
        return (self.low[0] + self.high[0]) / 2
        
        