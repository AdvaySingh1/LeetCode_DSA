
""" Look at the options within the tabular apprach. They closely resemble the memoization apprach and the different cases. 
    This can be used to visualize the repeated work within the table.

    This is the core concept behind dynamic programming.
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # see how different they are?
        cache = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            cache[i][0] = i
        for i in range(len(word2) + 1):
            cache[0][i] = i

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    cache[i][j] = cache[i-1][j-1]
                else:
                    cache[i][j] = 1 + min(cache[i-1][j-1], cache[i-1][j], cache[i][j-1])
        return cache[-1][-1]

        # memoization
        cache = [[-1] * len(word2) for _ in range(len(word1))]
        def memo(i1, i2):
            if i1 == len(word1) and i2 == len(word2):
                return 0
            if (i2 == len(word2)):
                return len(word1) - i1
            if (i1 == len(word1)):
                return len(word2) - i2
            if cache[i1][i2] != -1:
                return cache[i1][i2]
            
            if word1[i1] == word2[i2]:
                cache[i1][i2] = memo(i1+1, i2+1)
            else:
                cache[i1][i2] = 1 + min(memo(i1+1, i2), memo(i1, i2+ 1), memo(i1+1, i2+1))
            return cache[i1][i2]
        
        return memo(0, 0)

        # brute Force solution O(n + m) space and O(3^(n + m)) time
        def bruteForce(i1, i2):
            if i1 == len(word1) and i2 == len(word2):
                return 0
            if (i2 == len(word2)):
                return len(word1) - i1
            if (i1 == len(word1)):
                return len(word2) - i2
            
            if word1[i1] == word2[i2]:
                return bruteForce(i1+1, i2+1)

            return 1 + min(bruteForce(i1+1, i2), bruteForce(i1, i2+ 1), bruteForce(i1+1, i2+1))
        
        return bruteForce(0, 0)