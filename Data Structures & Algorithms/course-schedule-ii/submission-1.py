class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        queue = deque([course for course in range(numCourses) if in_degree[course] == 0])
        processed = 0
        while queue:
            node = queue.popleft()
            processed += 1
            res.append(node)
            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        return res if numCourses == processed else []