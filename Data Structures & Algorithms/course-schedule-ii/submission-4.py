class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for a, b in prerequisites:
            indegree[a] += 1
            graph[b].append(a)
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        while queue:
            node = queue.popleft()
            ans.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return ans if len(ans) == numCourses else []