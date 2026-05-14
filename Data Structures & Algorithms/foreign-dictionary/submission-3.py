class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        graph = defaultdict(set)
        in_degree = {c: 0 for word in words for c in word}
        for i in range(n - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        in_degree[c2] += 1
                    break
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        if len(res) != len(in_degree):
            return ""
        return ''.join(res)