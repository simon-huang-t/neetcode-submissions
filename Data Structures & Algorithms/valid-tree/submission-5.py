class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.sizes = [1] * n
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return 0
        if self.sizes[root_a] >= self.sizes[root_b]:
            self.parent[root_b] = root_a
            self.sizes[root_a] += self.sizes[root_b]
        else:
            self.parent[root_a] = root_b
            self.sizes[root_b] += self.sizes[root_a]
        return 1


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        dsu = DSU(n)
        components = n
        for a, b in edges:
            components -= dsu.union(a, b)
        return components == 1
        