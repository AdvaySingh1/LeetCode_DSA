
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        """ The dynamic programming (memorization) top down approach """
        dp = [0 for i in range(n + 1)]

        for i in range(1, n + 1):
            count = 0
            if i % 2 == 1:
                count += 1
            
            dp[i] = dp[i // 2] + count
        
        return dp



        """ The following is the brute force approach with an O(nlogn) time complexity """
        res = []

        for i in range(n + 1):
            p = i
            count = 0
            while p > 0:
                if p % 2 == 1:
                    count += 1
                p = p // 2
            res.append(count)
        
        return res


    """ O(n) method to reverse the bits for the int """

    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res += bit << (31 - i)
        
        return res