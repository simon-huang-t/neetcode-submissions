class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        transformations = 1
        queue = deque([beginWord])
        visited = set({beginWord})
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == endWord:
                    return transformations
                for i, c in enumerate(node):
                    for j in range(ord('a'), ord('a') + 26):
                        letter = chr(j)
                        if letter == c:
                            continue
                        new_word = node[:i] + letter + node[i+1:]
                        if new_word in word_set and new_word not in visited:
                            queue.append(new_word)
                            visited.add(new_word)

            transformations += 1
        return 0