class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def buildTrie():
            root = TrieNode()
            for word in words:
                node = root
                for c in word:
                    if c not in node.children:
                        node.children[c] = TrieNode()
                    node = node.children[c]
                node.word = word
            return root

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        
        def dfs(node, r, c):
            char = board[r][c]
            if char not in node.children:
                return
            next_node = node.children[char]
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None
            board[r][c] = '#'
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#':
                    dfs(next_node, nr, nc)
            board[r][c] = char

        m, n = len(board), len(board[0])
        res = []
        root = buildTrie()
        for r in range(m):
            for c in range(n):
                dfs(root, r, c)
        return res

