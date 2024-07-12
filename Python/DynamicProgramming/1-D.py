""" Climbing stairs
"""


class Solution:
    def __init__(self):
        self.cache = {}

    def climbStairs(self, n: int) -> int:
        """bottom up dynamic programming O(n) time and O(1) space"""
        if n <= 2:
            return n
        
        arr = [1, 2]
        for i in range(3, n + 1):
            temp = arr[1]
            arr[1] = arr[0] + arr[1]
            arr[0] = temp
        
        return arr[1]
        


        """top down dynamic programming using memorization O(n) time and O(n) space"""
        # if n <= 2:
        #     return n
        # elif n in self.cache:
        #     return self.cache[n]
        
        # else:
        #     self.cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        # return self.cache[n]

        """Brute Force O(2^n) with O(n) space"""
        # if n <=2:
        #     return n
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        