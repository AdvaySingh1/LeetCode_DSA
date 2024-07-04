"""
Demonstrates the case when you need to find the minimum number for something rather than the number itself.
One approach is to keep decreasing when even the value below it is lower.
This one offers a faster solution. Keep setting the res and if that value happens to be the lowest, the l will increment up.
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
    

        while (l <= r):
            k, hours = l + ((r - l)//2), 0

            for p in piles:
                hours += math.ceil(float(p) / k)

            if hours > h:
                l = k + 1
            else:
                res = k
                r = k - 1
                
        return res
