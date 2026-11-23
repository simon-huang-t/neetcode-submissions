class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        queue = deque([beginWord])
        transformations = 1
        visited = set({beginWord})
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return transformations
                for i, c in enumerate(word):
                    for j in range(ord('a'), ord('a') + 26):
                        letter = chr(j)
                        if letter == c:
                            continue
                        new_word = word[:i] + letter + word[i+1:]
                        if new_word not in visited and new_word in word_set:
                            queue.append(new_word)
                            visited.add(new_word)
            transformations += 1
        return 0