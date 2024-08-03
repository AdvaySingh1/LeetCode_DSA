class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        #O (n * m * p) time and space tabular solution (can be optimized to O(n * m)).
        cache = [[[False] * (len(s1) + 1) for _ in range(len(s2) + 1)] for _ in range(len(s3) + 1)]
        cache[0][0][0] = True
        # need to start with 0 for certain conditions (when one is the same as the other it should be true).
        for i3 in range(1, len(cache)):
            for i2 in range(len(cache[0])):
                for i1 in range(len(cache[0][0])):
                    if i1 >= 1 and s1[i1 - 1] == s3[i3 - 1]:
                        cache[i3][i2][i1] = cache[i3 - 1][i2][i1 - 1]
                    if i2 >= 1 and s2[i2 - 1] == s3[i3 - 1]:
                        cache[i3][i2][i1] = cache[i3][i2][i1] or cache[i3 - 1][i2 - 1][i1]
        return cache[-1][-1][-1]

        # O(n * m * p) solution time and space
        cache = {} # (i1, i2, i3)
        def memo(i1, i2, i3):
            if i3 == len(s3):
                if (i1 == len(s1) and i2 == len(s2)):
                    return True 
                return False
            if (i1, i2, i3) in cache:
                return cache[(i1, i2, i3)]

            if i1 < len(s1) and s1[i1] == s3[i3]:
                if i2 < len(s2) and s2[i2] == s3[i3]:
                    cache[(i1, i2, i3)] = memo(i1 + 1, i2, i3 + 1) or memo(i1, i2 + 1, i3 + 1)
                else:
                    cache[(i1, i2, i3)] = memo(i1 + 1, i2, i3 + 1)

            elif i2 < len(s2) and s2[i2] == s3[i3]:
                cache[(i1, i2, i3)] = memo(i1, i2 + 1, i3 + 1)
            
            return cache[(i1, i2, i3)] if (i1, i2, i3) in cache else False

        return memo(0, 0, 0)
        # brute force O(n + m) solution of O(p) space where p is the min length between s1 and s2 and s3
        # O(2^p) time solution.
        def bruteForce(i1, i2, i3):
            print(i1, i2, i3)
            if i3 == len(s3):
                if (i1 == len(s1) and i2 == len(s2)):
                    return True 
                return False

            if i1 < len(s1) and s1[i1] == s3[i3]:
                if i2 < len(s2) and s2[i2] == s3[i3]:
                    return bruteForce(i1 + 1, i2, i3 + 1) or bruteForce(i1, i2 + 1, i3 + 1)
                return bruteForce(i1 + 1, i2, i3 + 1)

            elif i2 < len(s2) and s2[i2] == s3[i3]:
                return bruteForce(i1, i2 + 1, i3 + 1)
            
            return False
        
        return bruteForce(0, 0, 0)

        