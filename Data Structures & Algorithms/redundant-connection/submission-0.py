class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA == rootB:
            return False
        if self.size[rootA] > self.size[rootB]:
            self.size[rootA] += self.size[rootB]
            self.parent[rootB] = rootA
        else:
            self.size[rootB] += self.size[rootA]
            self.parent[rootA] = rootB

        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n)
        for a, b in edges:
            if not dsu.union(a, b):
                return [a, b]
