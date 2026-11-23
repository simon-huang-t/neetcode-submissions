class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1] * n

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return 0
        if self.sizes[root_a] > self.sizes[root_b]:
            self.parents[root_b] = root_a
            self.sizes[root_a] += self.sizes[root_b]
        else:
            self.parents[root_a] = root_b
            self.sizes[root_b] += self.sizes[root_a]
        return 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = n
        dsu = DSU(n)
        for a, b in edges:
            components -= dsu.union(a, b)
        return components
        