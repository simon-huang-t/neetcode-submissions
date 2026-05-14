class DSU:
    def __init__(self, n):
        self.root = list(range(n))
        self.sizes = [1] * n

    def find_root(self, node):
        if self.root[node] != node:
            self.root[node] = self.find_root(self.root[node])
        return self.root[node]

    def union(self, a, b):
        root_a, root_b = self.find_root(a), self.find_root(b)
        if root_a == root_b:
            return 0
        if self.sizes[root_a] < self.sizes[root_b]:
            self.root[root_a] = root_b
            self.sizes[root_b] += self.sizes[root_a]
        else:
            self.root[root_b] = root_a
            self.sizes[root_a] += self.sizes[root_b]
        return 1


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        dsu = DSU(n)
        components = n
        for a, b in edges:
            components -= dsu.union(a, b)
        if components == 1:
            return True
        return False





        