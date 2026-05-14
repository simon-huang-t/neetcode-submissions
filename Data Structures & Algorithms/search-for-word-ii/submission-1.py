
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = [(-1, 0), (1, 0), (0, -1), (0,  1)]
        def buildTrie():
            root = TrieNode()
            for word in words:
                node = root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.word = word
            return root
        
        def dfs(node, r, c):
            char = board[r][c]
            if char not in node.children:
                return
            next_node = node.children[char]
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None
            board[r][c] = '#'
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(next_node, nr, nc)
            board[r][c] = char
        
        root = buildTrie()
        result = []
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                dfs(root, r, c)
        return result