from typing import List

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # dynamic programming O(n * m) time and O(m) space solution
        cache = [0 for m in range(capacity + 1)]

        for i in range(len(cache)):
            if i - weight[0] >= 0:
                cache[i] = profit[0]
            
        for i in range(1, len(profit)):
            curr_cache = [0 for m in range(capacity + 1)]
            for j in range(1, capacity + 1):
                # exlude
                exclude = cache[j]

                # include
                if j - weight[i] >= 0:
                    include = profit[i] + cache[j - weight[i]]
                    exclude = max(exclude, include)
                curr_cache[j] = exclude

            print (curr_cache)
            cache = curr_cache
        
        return cache[capacity]


        # dynamic programming O(n * m) solution
        # cache = [[0 for m in range(capacity + 1)] for n in range(len(profit))]

        # for i in range(len(cache[0])):
        #     if i - weight[0] >= 0:
        #         cache[0][i] = profit[0]
        
        # for i in range(1, len(cache)):
        #     for j in range(1, len(cache[0])):
        #         # not include
        #         exclude = cache[i - 1][j]

        #         # include
        #         if j - weight[i] >= 0:
        #             include = profit[i] + cache[i - 1][j - weight[i]]
        #             exclude = max(exclude, include)
                
        #         cache[i][j] = exclude

        # return cache[len(profit) - 1][capacity]




        # memorization O(n * m) solution
        # cache = [[-1 for m in range(capacity + 1)] for n in range(len(profit))]

        # def dfs(i, cap):
        #     if i == len(profit):
        #         return 0
        #     if cache[i][cap] != -1:
        #         return cache[i][cap]
            
        #     # without including
        #     cache[i][cap] = dfs(i + 1, cap)

        #     # with including
        #     newCap = cap - weight[i]
        #     if newCap < 0:
        #         return cache[i][cap]
        #     p = profit[i] + dfs(i + 1, newCap)
        #     cache[i][cap] = max(p, cache[i][cap])

        #     return cache[i][cap]

        # return dfs(0, capacity)




        # brute force O(2^n) solution

        # def dfs(i, cap):
        #     if i == len(profit):
        #         return 0
            
        #     # case where you don't include
        #     p1 = dfs(i + 1, cap)

        #     # care were you do include
        #     newCap = cap - weight[i]
        #     if newCap < 0:
        #         return p1
        #     p2 = profit[i] + dfs(i + 1, newCap)

        #     return max(p1, p2)


        # return dfs(0, capacity)