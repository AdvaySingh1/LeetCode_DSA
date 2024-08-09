class Solution:

    """ Great dynamic programming example with different base case (in range).
        See picture from 08/05/2024.
    """
    def longestPalindromeSubseq(self, s: str) -> int:

        #true dynamic programming solution
        cache = [[0] * len(s) for _ in range(len(s))]

        # establish the base case
        for i in range(len(cache)):
            cache[i][i] = 1

        for subseq in range(2, len(s) + 1):
            for i in range(len(s) - subseq + 1):
                j = i + subseq - 1
                if s[i] == s[j]:
                    cache[i][j] = 2 + cache[i+1][j-1]
                else:
                    cache[i][j] = max(cache[i][j-1], cache[i+1][j])
        return cache[0][len(s)-1]

        
        # O(n^2) time and space complexity solution
        cache = {} # (i, j)
        def memo(i, j):
            if i == j:
                return 1
            if i > j:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            elif s[i] == s[j]:
                cache[(i, j)] = 2 + memo(i+1, j-1)
            else:
                cache[(i, j)] = max(memo(i, j-1), memo(i+1, j))
            return cache[(i, j)]
            
        return memo(0, len(s)-1)

        # O(3^n) time complexty brute force solution
        def bruteForce(i, j):
            if i == j:
                return 1
            elif i < 0 or j >= len(s):
                return 0
            elif s[i] == s[j]:
                return 1+max(bruteForce(i+1, j+1), bruteForce(i+1, j))
            else:
                return max(bruteForce(i, j+1), bruteForce(i+1, j+1), bruteForce(i+1, j))

        return bruteForce(0, 1)
            
            

        return memo(0, 1)
            

        def helper(l, r, sub):
            while l >= 0 and r < len(sub) and sub[l] == sub[r]:
                l -= 1
                r += 1
            return r - l - 1
        

        # dynamic programming for all of the subsequences
        # all possible substrings
        def bruteForce(i, substr):
            if i == len(s):
                res = 0
                for j in range(len(substr)):
                    res = max(res, helper(j, j, substr))
                    res = max(res, helper(j, j + 1, substr))
                return res

            res = bruteForce(i + 1, substr)
            res = max(res, bruteForce(i + 1, substr + s[i]))
            return res

        return bruteForce(0, "")





        def bruteForce(i, substr, res):
            if i == len(s):
                if len(substr) == 2:
                    if substr[0] == substr[1]:
                        res = max(res, len(substr))
                else:
                    res = max(res, len(substr))
                return res
            
            
            if len(substr) > 1:
                if s[i] == substr[0]:
                    res = max(res, bruteForce(i + 1, substr+s[i], res))
                else:
                    res = max(res, bruteForce(i + 1, substr, res))
                    
            else:
                res = max(res, bruteForce(i + 1, substr, res))
                res = max(res, bruteForce(i + 1, substr+s[i], res))

            return res
                

        return bruteForce(0, "", 1)

















        def helper(l, r, res):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res = max(res, r - l + 1)
                l-=1
                r+=1
            return res
        
        for i in range(len(s)):
            res = helper(i, i, res)
            res = helper(i, i+1, res)

        return res


# the first apprach yeuilds O(2^n) possible solutions. 
# Then going through each and stermining if they are palindromes is O(n^2).
# hence the brute force time complexity of O(n^2 * 2^n).
# Is there an O(n^2) solution?