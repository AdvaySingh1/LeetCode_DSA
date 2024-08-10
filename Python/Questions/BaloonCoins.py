class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        """ Tabular solution with permutations. Right greater than left. """
        """ Similar to subsets with palindromes. """
        # Tabular solution
        nums = [1] + nums + [1]
        cache = {} # (l, r)

        for offset in range(2, len(nums)):
            for left in range(len(nums) - offset):
                right = left + offset
                for pivot in range(left + 1, right):
                    coins = nums[pivot] * nums[left] * nums[right]
                    coins += cache.get((left, pivot), 0) + cache.get((pivot, right), 0)

                    cache[(left, right)] = max(coins, cache.get((left, right), 0))

        return cache.get((0, len(nums) - 1), 0)


        # Memoization solution
        # O(n^2) for all possible combinatinos of l and r. * n each time hence O(n^3) time.
        # O(n^2) for space.
        nums = [1] + nums + [1]
        cache = {} # (l, r)

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in cache:
                return cache[(l, r)]

            cache[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dfs(l, i-1) + dfs(i+1, r)
                cache[(l, r)] = max(coins, cache[(l, r)])

            return cache[(l, r)]
        
        return dfs(1, len(nums) - 2)


