""" Floyed O(n) time and O(1) space algorithm to find the start of the cycle """
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        
        slow2 = 0

        while nums[slow2] != nums[slow]:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return nums[slow]