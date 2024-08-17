from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ Given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
        You may buy and sell one NeetCoin multiple times with the following restrictions:
        After you sell your NeetCoin, you cannot buy another one on the next day (i.e., there is a cooldown period of one day).
        You may only own at most one NeetCoin at a time.
        You may complete as many transactions as you like.

        Args:
            prices (List[int]): prices of the market on the respective days.

        Returns:
            int: the maximum profit you can achieve.
        """
        # like knapsack

        cache = {} # n space and time
        def dfs(i, neetCoins):
            if i >= len(prices):
                return 0
            
            if (i, neetCoins) in cache:
                return cache[(i, neetCoins)]
            
            # time to sell
            if neetCoins:
                cache[(i, neetCoins)] = max(dfs(i + 1, True), dfs(i + 2, False) + prices[i])

            # time to buy
            else:
                cache[(i, neetCoins)] = max(dfs(i + 1, True) - prices[i], dfs(i + 1, False))
            return cache[(i, neetCoins)]
            
        return dfs(0, False)

            
            
