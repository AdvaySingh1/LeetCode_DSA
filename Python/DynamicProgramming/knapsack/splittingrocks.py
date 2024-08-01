from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        # fastest apprach
        # tabular O(m) solution
        target = sum(stones) // 2
        vals = [0] * (target + 1)
        for stone in stones:
            for i in range(target, stone - 1, -1):
                vals[i] = max(vals[i], vals[i - stone] + stone)
        return sum(stones) - vals[-1] - vals[-1]

        
        # this question is permutations not just combinations
        # Going tabular O(n * sum(n))
        target = sum(stones) / 2

        # memoization approach O(n * sum(n))
        cache = {} # (i, total)
        def dfs(i, total):
            if i == len(stones):
                return abs(total - target)
            if (i, total) in cache:
                return cache[(i, total)]

            # exclude vs include
            cache[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))

            return cache[(i, total)]

        return int(dfs(0, 0) * 2)


        # find a subarray closes to half the sum of the array
        res = [0]
        for stone in stones:
            new_res = res.copy()
            for val in res:
                newVal = val + stone
                if val + stone == target:
                    return 0
                    # include 
                new_res.append(newVal)
            res = new_res
    

        min_diff = float("inf")
        for val in res:
            min_diff = min(abs(val - target), min_diff)
        
        return int(min_diff * 2)
        
            