import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.posts = defaultdict(list) # a list of tweets [-time, id] for python
        self.followMap = defaultdict(set) # set of users
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # using heap algorithm although overall same time complexity as 10
        # this would be more effecient if we needed the j most recent instead of 10
        self.followMap[userId].add(userId)
        heap, res = [], []

        # O(n) to create the heap
        for followee in self.followMap[userId]:
            for post in self.posts[followee]:
                heap.append(post)
            
        # time complexity O(n)
        heapq.heapify(heap)

        for i in range(10):
            if not heap:
                break
            count, tweetId = heapq.heappop(heap)
            res.append(tweetId)
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
