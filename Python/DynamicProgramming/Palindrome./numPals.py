class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        # helper (each index)
        def helper(l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l-=1
                r+=1
            return res

        # even and odd
        for i in range(len(s)):
            res += helper(i, i)
            res += helper(i, i + 1)
        
        return res