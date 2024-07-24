from typing import List

""" /**
 * Duplicate subsets
 *
 * The time complexity comes from copying the leaf nodes and it's n 2^n because at each step, there are two decisions and therefore 2^n
 */
 
 """


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        vals = []

        nums.sort() # O(nlog n) 

        def subsetsHelper(vals, i):
            if i >= len(nums):
                res.append(vals[:])
                return


            vals.append(nums[i])
            subsetsHelper(vals, i + 1)
            vals.pop()
            
            while (i + 1 in range(len(nums)) and nums[i] == nums[i + 1]):
                i += 1

            subsetsHelper(vals, i + 1)

        subsetsHelper(vals, 0)
        return res