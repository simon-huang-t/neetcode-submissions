class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        queue = deque([(0, -1)])
        visited = set({0})
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