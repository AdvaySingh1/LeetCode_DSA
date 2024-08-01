from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float("inf") for i in range(amount + 1)]
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins: # can be problamatic if amount < coin?
                if coin in range(len(dp)):
                    if i - coin >= 0:
                        dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        return dp[amount] if dp[amount] != float("inf") else -1





        # can't solve this with a greedy approach.
        """ When can you solve something with a greedy vs non-greedy approach."""

        # tabular solution O(n * m) solution
        # fastest apprach for bound and unbound questions trying to equal a certain value
        # for bound, look at splitting rocks. Iterate through coins on outside and cache on inside.
        cache = {m : float("inf") for m in range(amount + 1)}
        cache[0] = 0
        for i in range(len(cache)):
            for coin in coins:
                if i - coin >= 0:
                    cache[i] = min(cache[i], cache[i - coin] + 1)

        res = cache[amount]
        return res if res != float("inf") else -1

    

        # memoization would be O(n * m) solution (unbound version)
        cache = {} # O(m) space for the amount
        def bruteForce(amount): # i is the number of coins used
            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]
            
            min_coins = float("inf")
            for coin in coins:
                if amount - coin >= 0:
                    min_coins = min(min_coins, 1 + bruteForce(amount - coin))
            cache[amount] = min_coins
            return cache[amount]
        
        res = bruteForce(amount)
        return -1 if res == float("inf") else res

        
       



        """ 
        The following are kin to bound knapsack.
        Essentially, they are O(2^m) rather than O(n^m),
        """

        # abount modified


        # memoization solution O(n * m) time and space
        cache = {} # (i, amount)
        def memoization(i, amount):
            if i == len(coins):
                return 0 if not amount else float("inf")
            
            if (i, amount) in cache:
                return cache[(i, amount)]
            
            # exclude
            p1 = memoization(i + 1, amount)
            p2 = float("inf")
            # include
            if amount - coins[i] >= 0:
                p2 = 1 + memoization(i, amount - coins[i])
            cache[(i, amount)] = min(p1, p2)
            return cache[(i, amount)]

        res = memoization(0, amount)
        return -1 if res == float("inf") else res


        # brute force solution O(2^m) time and O(m) space where m is the amount.
        def bruteForce(i, amount):
            if i == len(coins):
                 # if not combo, very large
                return 0 if not amount else float("inf")

            # exclude
            p1 = bruteForce(i + 1, amount)
            p2 = float("inf")

            # inlude
            if amount - coins[i] >= 0:
                p2 = 1 + bruteForce(i, amount - coins[i])
            
            return min(p1, p2)

        res = bruteForce(0, amount)
        return res if res != float("inf") else -1
            