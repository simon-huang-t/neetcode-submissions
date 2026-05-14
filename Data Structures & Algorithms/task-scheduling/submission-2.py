class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        f = max(counts.values())
        k = sum(1 for v in counts.values() if v == f)
        return max(len(tasks), (f - 1) * (n + 1) + k)