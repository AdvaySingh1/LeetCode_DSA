from typing import List

""" The frist two solutions are the new means while the rest alter the bound knapsack question. """
""" Implementations are in order of most to least effecient. """

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        # tabular O(m) space and O(n * m) time solution
        cache = {}
        for m in range(capacity + 1):
            cache[m] = 0
            for n in range(len(profit)):
                if m - weight[n] >= 0:
                    cache[m] = max(cache[m], profit[n] + cache[m - weight[n]])
        return cache[capacity]

        # memoization solution O(m) space O(n * m) time
        cache = {} # m for capacity
        def memoization(cap):
            if cap == 0:
                return 0
            if cap in cache:
                return cache[cap]
            cache[cap] = 0
            for i in range(len(profit)):
                if (cap - weight[i] >= 0):
                    cache[cap] = max(cache[cap], profit[i] + memoization(cap - weight[i]))
            return cache[cap]
        return memoization(capacity)
                

        # tabular O(n * m) time and O(m) space solution. Same as Bound Knapsack
        cache = [0] * (capacity + 1)
        
        for i in range(len(profit)):
            newCache = [0] * (capacity + 1)
            # exclude
            for cap in range(capacity + 1):
                # exclude
                p1 = cache[cap]
                p2 = 0
                # include 
                if cap - weight[i] >= 0:
                    #p2 = profit[i] + cache[cap - weight[i]]  #for the bound knapsack
                    p2 = profit[i] + newCache[cap - weight[i]]
                newCache[cap] = max(p1, p2)
            cache = newCache

        return cache[-1]

        # tabular O(n * m) time and space solution. Same as Bound Knapsack.
        cache = [[0 for m in range(capacity + 1)] for n in range(len(profit))]

        # init the first row
        for cap in range(len(cache[0])):
            if cap - weight[0] >= 0:
                cache[0][cap] = profit[0] + cache[0][cap - weight[0]] # add as many times as you can
        # init the rest of the array
        for i in range(1, len(profit)):
            for cap in range(1, capacity + 1):
                # exclude
                p1 = cache[i - 1][cap]
                p2 = 0

                # include
                if cap - weight[i] >= 0:
                    #p2 = profit[i] + cache[i - 1][cap - weight[i]] for bound
                    p2 = profit[i] + cache[i][cap - weight[i]]
                cache[i][cap] = max(p1, p2)
            
        print(cache)

        return cache[-1][-1]


        # memoization O(n * m) time and space solution. Same as Bound Knapsack.
        cache = {} # (i, cap) which is why n * m. Can be 2-D array
        def memoization(i, cap) -> int:
            if i == len(profit):
                return 0
            if (i, cap) in cache:
                return cache[(i, cap)]
            
            # exclude
            cache[(i, cap)] = memoization(i + 1, cap)
            # include any number of times
            if cap - weight[i] >= 0:
                cache[(i, cap)] = max(cache[(i, cap)], profit[i] + memoization(i, cap - weight[i]))
            
            return cache[(i, cap)]
        
        return memoization(0, capacity)


        # brute force O(2 ^ c) time and O(c) space solution (Tree height depends on c now)
        def bruteForce(i, cap) -> int:
            if i == len(profit):
                return 0
            
            # exclude
            p1 = bruteForce(i + 1, cap)
            p2 = 0

            # include any number of times
            if cap - weight[i] >= 0:
                p2 = profit[i] + bruteForce(i, cap - weight[i])
            
            return max(p1, p2)
        
        return bruteForce(0, capacity)


