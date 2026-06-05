class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        def find_parent(node):
            if node != parent[node]:
                parent[node] = find_parent(parent[node])
            return parent[node]
        graph = defaultdict(list)
        for a, b in edges:
            root_a, root_b = find_parent(a), find_parent(b)
            if root_a == root_b:
                return [a, b]
            parent[root_b] = root_a
            
        
