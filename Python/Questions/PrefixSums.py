""" For ranged based calculations:
"""

""" O(n) O(1) after initialization time complexity vs O(q * n) where q is the number of queries"""

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.pre = []
        total = 0
        for n in nums:
            total += n
            self.pre.append(total)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right] - (self.pre[left - 1] if left - 1 >= 0 else 0)
    



""" O(1) apprach for 2-D grid with O(1) """

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prev = [[0 for i in range(len(matrix[0]) + 1)] for i in range(len(matrix) + 1)]

        for r in range(len(matrix)):
            total = 0
            for c in range(len(matrix[0])):
                total += matrix[r][c]
                above = self.prev[r][c + 1]

                self.prev[r + 1][c + 1] = total + above
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        s = 0

        b_r = self.prev[row2 + 1][col2 + 1]
        b_l = self.prev[row2 + 1][col1]
        t_r = self.prev[row1][col2 + 1]
        t_l = self.prev[row1][col1]

        return b_r - b_l - t_r + t_l




        # for i in range(row1, row2 + 1):
        #     s += self.prev[i][col2] - (self.prev[i][col1] if col1 >= 0 else 0)
        
        # return s
        

""" O(n) time and space solution for the number of subarrays which add to a certain value"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = {0: 1}
        count = 0
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s - k in pre:
                count += pre[s - k]
            pre[s] = 1 + pre.get(s, 0)
        
        return count

