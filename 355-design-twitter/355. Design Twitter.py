class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list)
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res, heap = [], []
        self.follow_map[userId].add(userId)

        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId]) - 1
                time, tweetId = self.tweet_map[followeeId][index]
                heap.append((time, tweetId, followeeId, index-1))
            
        heapq.heapify(heap)

        while heap and len(res) < 10: 
            time, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)

            if index >= 0:
                time, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(heap, (time, tweetId, followeeId, index-1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)