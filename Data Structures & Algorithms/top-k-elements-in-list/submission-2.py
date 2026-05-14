class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        min_heap = []
        for value, count in count.items():
            heapq.heappush(min_heap, (count, value))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [value for _, value in min_heap]




















        count = Counter(nums)
        n = len(nums)
        bucket = [[] for _ in range(n + 1)]
        for value, frequency in count.items():
            bucket[frequency].append(value)
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for value in bucket[i]:
                res.append(value)
                if len(res) == k:
                    return res
        
