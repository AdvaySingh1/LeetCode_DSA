from typing import List

""" Permutations with duplicates """

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        if not nums:
            return [[]]

        nums.sort()

        val = nums.pop()

        perms = self.permuteUnique(nums)

        for p in perms: # O((n - 1)!)
            for j in range(len(p) + 1):
                if j in range(1, len(p)) and p[j - 1] == val:
                    continue

                perm = p.copy()
                perm.insert(j, val)
                res.append(perm[:]) # O(n)

                if j < len(p) and p[j] == val:
                    break

            

        return res

    
        
        