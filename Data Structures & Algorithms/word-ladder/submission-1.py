class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        groupsList = defaultdict(list)
        L = len(beginWord)
        for word in word_set:
            for i in range(L):
                generic_word = word[:i] + '*' + word[i+1:]
                groupsList[generic_word].append(word)
        queue = deque([beginWord])
        visited = set({beginWord})
        transformations = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return transformations
                for i in range(L):
                    generic_word = word[:i] + '*' + word[i+1:]
                    for new_word in groupsList[generic_word]:
                        if new_word not in visited and new_word in word_set:
                            visited.add(new_word)
                            queue.append(new_word)

            transformations += 1

        
        return 0
