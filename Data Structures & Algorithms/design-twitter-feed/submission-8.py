class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.following[userId].add(userId)
        for followee in self.following[userId]:
            tweets = self.tweets[followee]
            for time, tweetId in tweets:
                heapq.heappush(heap, (time, tweetId))
                if len(heap) > 10:
                    heapq.heappop(heap)
        heap.sort(key = lambda x: -x[0])
        return [tweetId for _, tweetId in heap]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
