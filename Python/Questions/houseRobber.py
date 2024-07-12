from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """ Dynamic Programming apprach O(n) time and O(1) speed."""
        n1, n2 = 0, 0

        for n in nums:
            tmp = n2
            n2 = max(n2, n1 + n)
            n1 = tmp
        
        return n2



        """ Brute force apprach """
        # if len(nums) == 0 or not nums:
        #     return 0
        
        # return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))