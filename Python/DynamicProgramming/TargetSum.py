from typing import List

""" You can add or subtract each of the values in the list and they have to equal the target value. """

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # tabular bottom up apprach. 2 * total is the time and space complexity
        # formally O(n * m) where m is the total
        # sums = [0]
        # for i in range(len(nums)):
        #     curr_sums = []
        #     for n in sums:
        #         curr_sums.append(n + nums[i])
        #         curr_sums.append(n - nums[i])
        #     sums = curr_sums
        # count = 0
        # for n in curr_sums:
        #     if n == target:
        #         count += 1
        
        # return count

        # O(n * sum(n)) time and space. The different totals there can be
        cache = {} # {index, total} -> number of ways with the index value
        def memoization(i, total) -> int:
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in cache:
                return cache[(i, total)]
            
            cache[(i, total)] = (memoization(i + 1, total + nums[i]) 
                                + memoization(i + 1, total - nums[i]))
            
            return cache[(i, total)]
        
        return memoization(0, 0)


        # burte force solution O(2^n) time and O(n) space
        # def bruteForce(i, curr_sum):
        #     if i == len(nums):
        #         if curr_sum == target:
        #             return 1
        #         return 0
                
            
        #     return (bruteForce(i + 1, curr_sum + nums[i]) +
        #              bruteForce(i + 1, curr_sum - nums[i]))
        
        #return bruteForce(0, 0)

            
            

        