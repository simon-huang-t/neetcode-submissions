class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = [] #max_heap
        res = []
        self.following[userId].add(userId) # Forgot
        for followeeId in self.following[userId]:
            tweets = self.tweets[followeeId]
            if tweets:
                idx = len(tweets) - 1
                time, tweetId = tweets[idx]
                heapq.heappush_max(heap, (time, tweetId, followeeId, idx - 1))
        while heap and len(res) < 10:
            time, tweetId, followeeId, idx = heapq.heappop_max(heap)
            res.append(tweetId)
            if idx >= 0:
                tweets = self.tweets[followeeId]
                newTime, newTweetId = tweets[idx]
                heapq.heappush_max(heap, (newTime, newTweetId, followeeId, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
