class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # optimized solution
        if len(str2) < len(str1):
            str1, str2 = str2, str1

        cache = [None] * (len(str2) + 1)
        for i in range(len(str2) + 1): # optimize later
            cache[i] = str2[:i]
        for i1 in range(1, len(str1) + 1):
            newCache = [None] * (len(str2) + 1)
            newCache[0] = str1[:i1]
            for i2 in range(1, len(str2) + 1):
                if str1[i1-1] == str2[i2-1]:
                    newCache[i2] = cache[i2-1] + str1[i1-1]
                else:
                    s1 = cache[i2]
                    s2 = newCache[i2-1]
                    if len(s2) < len(s1):
                        newCache[i2] = s2 + str2[i2-1]
                    else:
                        newCache[i2] = s1 + str1[i1-1]
            cache = newCache
        
        return cache[-1]


        # tabular one (not optimized)
        cache = [[""] * (len(str2) + 1) for _ in range(len(str1) + 1)]
        # properly init the cache
        for i1 in range(1, len(str1) + 1):
            cache[i1][0] = str1[:i1]
        for i2 in range(1, len(str2) + 1):
            cache[0][i2] = str2[:i2]


        for i1 in range(1, len(str1) + 1):
            for i2 in range(1, len(str2) + 1):
                if str1[i1-1] == str2[i2-1]:
                    cache[i1][i2] = cache[i1-1][i2-1] + str1[i1-1]
                else:
                    s1 = cache[i1-1][i2]
                    s2 = cache[i1][i2-1]
                    if len(s2) < len(s1):
                        cache[i1][i2] = s2 + str2[i2-1]
                    else:
                        cache[i1][i2] = s1 + str1[i1-1]
        
        return cache[-1][-1]


        # memo solution O(n * m) space and time
        cache = {} # (i1, i2)
        def memo(i1, i2):
            if i1 == len(str1):
                return str2[i2:]
            if i2 == len(str2):
                return str1[i1:]

            if (i1, i2) in cache:
                return cache[(i1, i2)]
            
            if str1[i1] == str2[i2]:
                cache[(i1, i2)] = str1[i1] + memo(i1 + 1, i2 + 1)
            
            else:
                s1 = str1[i1] + memo(i1 + 1, i2)
                s2 = str2[i2] + memo(i1, i2 + 1)

                if len(s2) < len(s1):
                    cache[(i1, i2)] = s2
                else:
                    cache[(i1, i2)] = s1

            return cache[(i1, i2)]

        return memo(0, 0)

        # brute force solution O(n + m) space and O(2^(n + m)) time.
        def bruteForce(i1, i2):
            if i1 == len(str1):
                return str2[i2:]
            if i2 == len(str2):
                return str1[i1:]
            
            if str1[i1] == str2[i2]:
                return str1[i1] + bruteForce(i1 + 1, i2 + 1)

            s1 = str1[i1] + bruteForce(i1 + 1, i2)
            s2 = str2[i2] + bruteForce(i1, i2 + 1)

            if len(s2) < len(s1):
                return s2
            return s1

        return bruteForce(0, 0)