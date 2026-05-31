class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        self.parent = list(range(n + 1))
        def find(node):
            if node != self.parent[node]:
                self.parent[node] = find(self.parent[node])
            return self.parent[node]
        for a, b in edges:
            root_a, root_b = find(a), find(b)
            if root_a == root_b:
                return [a, b]
            self.parent[root_b] = root_a
        