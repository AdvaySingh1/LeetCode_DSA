from typing import List

""" Greedy O(n) solution."""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goal:
                goal = i

        return True if goal == 0 else False

        j, i = nums[0] if nums else 0, 0
        while i < len(nums) - 1 and j > 0:
            maxJump, newInd = 0, 0
            for ind, n in enumerate(nums[i + 1: i + j + 1]):
                ind += i + 1
                if ind == len(nums) - 1:
                    return True
                if n + ind > maxJump + newInd:
                    maxJump, newInd = n, ind
            
            j, i = maxJump, newInd
        

        return True if i == len(nums) - 1 else False
        