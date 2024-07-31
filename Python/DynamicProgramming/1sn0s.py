from typing import List
from collections import defaultdict


""" Another example of O(2^n) time and O(n) space vs O(i * m * n) time and space. """
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # This solution can be optimized to only have the last row as the cache.
        # tabular O(p * m * n) space
        cache = defaultdict(int) # (i, m, n): size
        # init to default dict so first rows is all zeros
        for i in range(len(strs)):
            s = strs[i]
            z, o = s.count("0"), s.count("1")
            for zero in range(m + 1):
                for one in range(n + 1):
                    if z <= zero and o <= one:
                        cache[(i, zero, one)] = max(cache[(i - 1, zero, one)], 1 + cache[(i - 1, zero - z, one - o)])
                    else:
                        cache[(i, zero, one)] = cache[(i - 1, zero, one)]
        
        return cache[len(strs) - 1, m, n]


        

        # yeilded the fasted solution in this case

        # O(p * m * n) where p is the length of strs
        cache = {} # (i, m, n): size
        def memoization(i, zeros, ones):
            if i == len(strs):
                return 0
            if (i, zeros, ones) in cache:
                return cache[(i, zeros, ones)]
            
            # exclude
            cache[(i, zeros, ones)] = memoization(i + 1, zeros, ones)
            
            z, o = zeros, ones # need new values
            # include
            for c in strs[i]:
                if c == "1":
                    ones -= 1
                else:
                    zeros -= 1
            if ones >= 0 and zeros >= 0:
                cache[(i, z, o)] = max(cache[(i, z, o)], 1 + memoization(i + 1, zeros, ones))
            return cache[(i, z, o)]
            
        return memoization(0, m, n)

        
        # Brute Force (O(k * 2^p)) time and O(n) space where k is the 
        # average number of letters in the string
        def bruteForce(i, ones, zeros, size):
            if i == len(strs):
                return size
            # exclude
            p1 = bruteForce(i + 1, ones, zeros, size)
            # include
            for c in strs[i]:
                if c == "1":
                    ones -= 1
                else:
                    zeros -= 1
            if ones >= 0 and zeros >= 0:
                p1 = max(p1, bruteForce(i + 1, ones, zeros, size + 1))

            return p1

        
        return bruteForce(0, n, m, 0)
