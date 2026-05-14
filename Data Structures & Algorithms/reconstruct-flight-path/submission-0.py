class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse = True)
        edges = defaultdict(list)
        for s, d in tickets:
            edges[s].append(d)
        start = 'JFK'
        res = []
        def dfs(node):
            # for _ in range(len(edges[node])):
            while edges[node]:
                nei = edges[node].pop()
                dfs(nei)
            res.append(node)
        dfs(start)
        return res[::-1]
        

        


