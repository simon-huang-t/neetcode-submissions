class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        start = 'JFK'
        res = []
        tickets.sort(reverse = True)
        for s, d in tickets:
            adj[s].append(d)

        def dfs(node):
            while adj[node]:
                nei = adj[node].pop()
                dfs(nei)
            res.append(node)
        dfs(start)
        return res[::-1]