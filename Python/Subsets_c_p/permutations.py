from typing import List

""" The following is the recursive solution to permutations. """

""" The overall time complexity for this is O(n * n!)"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if not nums:
            return [[]]

        n = nums.pop(0)

        perms = self.permute(nums)

        # the following yields O(n!)

        """ There are n-1! perms. For each perm, we insert our number into n possible positions. Therefore O(n!). However,
            for each insertion, there is O(n) work required unless this is a linked list. Therefore, we have O(n * n!)."""

        for p in perms: # O((n - 1)!)
            for j in range(len(p) + 1):
                perm = p.copy()
                perm.insert(j, n)
                res.append(perm[:]) # O(n)


        return res
            