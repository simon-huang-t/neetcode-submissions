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
        heap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            tweets = self.tweetMap[followeeId]
            for count, tweetId in tweets:
                heapq.heappush(heap, (count, tweetId))
                if len(heap) > 10:
                    heapq.heappop(heap)
        heap.sort(key = lambda x: -x[0])
        return [tweetId for _, tweetId in heap]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
        
