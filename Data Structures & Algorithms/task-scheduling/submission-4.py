class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        f = max(count.values())
        k = sum(1 for v in count.values() if v == f)
        return max(len(tasks), (f - 1) * (n + 1) + k)