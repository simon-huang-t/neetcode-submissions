class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        queue = deque([(0, -1)])
        visited = set()
        visited.add(0)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        while queue:
            node, par = queue.popleft()
            for nei in graph[node]:
                if nei == par:
                    continue
                if nei in visited:
                    return False
                visited.add(nei)
                queue.append((nei, node))
        return len(visited) == n