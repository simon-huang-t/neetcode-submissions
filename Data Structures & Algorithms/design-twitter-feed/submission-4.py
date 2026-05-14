# Follower --> Followee
class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set) # userId --> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = [] # max_heap
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            tweets = self.tweetMap[followeeId]
            if tweets:
                idx = len(tweets) - 1
                time, tweetId = tweets[idx]
                heapq.heappush_max(heap, (time, tweetId, followeeId, idx - 1))
        while heap and len(res) < 10:
            count, tweetId, followeeId, idx = heapq.heappop_max(heap)
            res.append(tweetId)
            if idx >= 0:
                nextCount, nextTweetId = self.tweetMap[followeeId][idx]
                heapq.heappush_max(heap, (nextCount, nextTweetId, followeeId, idx - 1))
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
        
