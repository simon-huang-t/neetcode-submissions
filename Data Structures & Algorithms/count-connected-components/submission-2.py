class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return 0
        if self.size[root_a] > self.size[root_b]:
            self.parent[root_b] = self.parent[root_a]
            self.size[root_a] += self.size[root_b]
        else:
            self.parent[root_a] = self.parent[root_b]
            self.size[root_b] += self.size[root_a]
        return 1
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = n
        dsu = DSU(n)
        for a, b in edges:
            components -= dsu.union(a, b)
        return components
        