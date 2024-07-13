from typing import List

""" The following is the dynamic programming (not O(n^2) checking every substring) implementaion of 
    longest substring where we can change k things within the array."""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        count = {}
        max_size = 0
        mRef = 0

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            mRef = max(mRef, count[s[R]])
            if ((R - L + 1) - mRef > k): # Can be done with .values() but increases to O(n^2)
                count[s[L]] -= 1
                L += 1
            max_size = max(max_size, R - L + 1)
        
        
        return max_size
        