class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # n = len(s)
        # dp = [False] * (n + 1)
        # word_set = set(wordDict)
        # for i in range(n - 1, - 1, -1):
        #     for word in word_set:
        #         if s.startswith(word, i) and dp[i + len(word)]:
        #             dp[i] = True
        #             break
        # return dp[0]

        words = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        for i in range(n - 1, - 1, -1):
            for word in words:
                if s.startswith(word, i) and dp[i + len(word)]:
                    dp[i] = True
                    break
        return dp[0]
