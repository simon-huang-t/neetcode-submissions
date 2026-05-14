class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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
        
