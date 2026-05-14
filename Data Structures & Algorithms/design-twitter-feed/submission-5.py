'''
The optimal solution for Design Twitter is:
- store tweets per user in chronological order
- use a heap for a k-way merge
- only process at most 10 tweets during feed generation

This avoids scanning every tweet ever posted.

Key Idea:
Each user's tweets are already sorted by time:
user 1 -> [old ... new]
user 2 -> [old ... new]

To generate the feed:
- take only the newest tweet from each followee
- put them into a max heap
- repeatedly pop the newest tweet
- then push that user's next older tweet

Exactly like merging k sorted lists.
'''
# Follower --> Followee
class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set) # userId --> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = [] # max_heap
        self.following[userId].add(userId)
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
                nexttime, nextTweetId = self.tweets[followeeId][idx]
                heapq.heappush_max(heap, (nexttime, nextTweetId, followeeId, idx - 1))
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
