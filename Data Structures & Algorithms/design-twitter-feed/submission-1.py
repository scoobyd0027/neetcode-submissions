import time
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.user_tweets = defaultdict(list)
        self.user_followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((time.time(), tweetId))
        if len(self.user_tweets[userId]) > 10:
            self.user_tweets[userId].pop(0)

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        self.user_followers[userId].add(userId)
        for follower_id in self.user_followers[userId]:
            tweets = self.user_tweets[follower_id]
            for time, tweetId in tweets:
                heapq.heappush(feed, (time, tweetId))
                if len(feed) > 10:
                    heapq.heappop(feed)
        
        res = []
        while feed:
            _, tweetId = heapq.heappop(feed)
            res.append(tweetId)
        
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_followers[followerId]:
            self.user_followers[followerId].remove(followeeId)
            

'''
1: [10]
2: [20]

1: 2

'''