from typing import List

""" The following is the recursive solution to permutations. """

""" The overall time complexity for this is O(n * n!)"""


 # the following yields O(n!)

""" There are n-1! perms. For each perm, we insert our number into n possible positions. Therefore O(n!). However,
            for each insertion, there is O(n) work required unless this is a linked list. Therefore, we have O(n * n!)."""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # non-recursive apprach with the same time and space complexity
        res = [[]]

        for num in nums:
            new_res = []
            for perm in res:
                for i in range(len(perm) + 1):
                    new_perm = perm.copy()
                    new_perm.insert(i, num)
                    new_res.append(new_perm)
            res = new_res
        
        return res
        
        
        # recursive apprach O(n * n!) because we make a copy and insert things for n! terms
        # Note this is the time complexity for n permute n which should be n!.
        # The space is O(n).
        # def p_helper(ns: List[int]) -> List[List[int]]:
        #     if not ns:
        #         return [[]]

        #     next_perm = p_helper(ns[1:])
        #     num = ns[0]

        #     res = []
        #     for perm in next_perm:
        #         for i in range(len(perm) + 1):
        #             new_perm = perm.copy()
        #             new_perm.insert(i, num)
        #             res.append(new_perm)
            
        #     return res
        
        # return p_helper(nums)
            