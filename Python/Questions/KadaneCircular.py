""" The following is a greedy ^ dynamic programming approach to solving the max subarray of a circular array
    Rather than a O(2^n) T, it is O(n) and the space complexity is O(1)."""

from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
 

        curr_min, curr_max, global_min, global_max, total = 0, 0, nums[0], nums[0], 0

        for n in nums:
            curr_min = min(curr_min, 0)
            curr_max = max(curr_max, 0)
            curr_min += n
            curr_max += n
            total += n

            global_min = min(global_min, curr_min)
            global_max = max(global_max, curr_max)
        
        if global_max > 0:
            total -= global_min
        
        return max(total, global_max)

