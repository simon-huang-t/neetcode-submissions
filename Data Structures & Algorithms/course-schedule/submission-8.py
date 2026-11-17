class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            indegree[a] += 1
            graph[b].append(a)
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        while queue:
            node = queue.popleft()
            numCourses -= 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return numCourses == 0