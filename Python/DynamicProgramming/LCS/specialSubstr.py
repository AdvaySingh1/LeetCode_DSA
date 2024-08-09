
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # tabular solution O(m) space and O(n * m) time
        cache = [0] * (len(t) + 1)
        cache[0] = 1
        for r in range(len(s)):
            newCache = [0] * (len(t) + 1)
            newCache[0] = 1
            for c in range(1, len(t) + 1):
                if (s[r] == t[c-1]):
                    newCache[c] = cache[c - 1] + cache[c]
                else:
                    newCache[c] = cache[c]
            cache = newCache
        return cache[len(t)]


        # tabular solution O(n * m) space and time
        cache = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            cache[i][0] = 1
        for r in range(1, len(s) + 1):
            for c in range(1, len(t) + 1):
                if (s[r-1] == t[c-1]):
                    cache[r][c] = cache[r - 1][c - 1] + cache[r - 1][c]
                else:
                    cache[r][c] = cache[r-1][c]
        return cache[len(s)][len(t)]

        # memo sol O(n * m) space and time
        cache = [[-1] * len(t) for _ in range(len(s))]
        def memo(i1, i2):
            if i2 == len(t):
                return 1
            if i1 == len(s):
                return 0
            if cache[i1][i2] != -1:
                return cache[i1][i2]

            cache[i1][i2] = 0

            if s[i1] == t[i2]:
                cache[i1][i2] += memo(i1 + 1, i2 + 1)
            cache[i1][i2] += memo(i1 + 1, i2)

            return cache[i1][i2]
        
        return memo(0, 0)

        # brute force solution O(n) space and O(2 ^(n)) time.
        def bruteForce(i1, i2):
            if i2 == len(t):
                return 1
            if i1 == len(s):
                return 0
            
            res = 0

            if s[i1] == t[i2]:
                res += bruteForce(i1 + 1, i2 + 1)
            res += bruteForce(i1 + 1, i2)

            return res
        
        return bruteForce(0, 0)