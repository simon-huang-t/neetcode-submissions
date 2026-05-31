class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.sizes = [1] * (n + 1)

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        if self.sizes[root_a] > self.sizes[root_b]:
            self.parent[root_b] = root_a
            self.sizes[root_a] = self.sizes[root_b]
        else:
            self.parent[root_a] = root_b
            self.sizes[root_b] = self.sizes[root_a]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n)
        for a, b in edges:
            if not dsu.union(a, b):
                return [a, b]
        