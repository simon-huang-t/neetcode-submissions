class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        groupList = defaultdict(list)
        L = len(beginWord)
        for word in word_set:
            for i in range(L):
                generic_word = word[:i] + '*' + word[i+1:]
                groupList[generic_word].append(word)
        transformations = 1
        queue = deque([beginWord])
        visited = set({beginWord})
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return transformations
                for i in range(L):
                    generic_word = word[:i] + '*' + word[i+1:]
                    for new_word in groupList[generic_word]:
                        

                # for i, c in enumerate(word):
                #     for j in range(ord('a'), ord('a') + 26):
                #         letter = chr(j)
                #         if letter == c:
                #             continue
                #         new_word = word[:i] + letter + word[i+1:]
                        if new_word in word_set and new_word not in visited:
                            queue.append(new_word)
                            visited.add(new_word)
            transformations += 1
        return 0