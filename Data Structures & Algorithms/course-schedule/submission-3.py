class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        queue = deque(node for node in range(numCourses) if in_degree[node] == 0)
        finish = 0
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
            finish += 1
        return finish == numCourses
        
