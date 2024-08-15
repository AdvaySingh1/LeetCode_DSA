from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """Determine the min cost in climbing stairs when we can climb either one or two stairs. 
           Done in O(n) time in tabular and memoization fashion.


        Args:
            cost (List[int]): The cost associated with each step.

        Returns:
            int: THe minimum cost.
        """
        # dp solution
        dp = [i for i in cost]
        for i in range(2, len(dp)):
            dp[i] += min(dp[i - 1], dp[i - 2])
        return min(dp[-1], dp[-2])



        # memoization solution
        cache = {}

        def dfs(i):
            if i >= len(cost):
                return 0

            if i in cache:
                return cache[i]
            
            cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return cache[i]
        
        return min(dfs(0), dfs(1))