class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        for a, b in edges:
            root_a, root_b = find(a), find(b)
            if root_a == root_b:
                return [a, b]
            parent[root_b] = root_a
        