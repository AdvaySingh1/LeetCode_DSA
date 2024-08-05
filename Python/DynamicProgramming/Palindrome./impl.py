""" The following is an O(n^2) implementation of determining the longest palindromic substring. It isn't tradiitonal dynamic programming
    but is nonetheless a good example of reducing repeated work.
    The brute force implementation goes through each substring (which is O(n^2)) and then iteraters through it with two pointers
    hence has a O(n^3) time complexity. This decreases the extra work."""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        # odd
        for i in range(len(s)):
            curr_res = s[i]
            l, r = i-1, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_res = s[l] + curr_res + s[r]
                l-=1
                r+=1
            if len(curr_res) > len(res):
                res = curr_res
        
        # even
        for i in range(len(s) - 1):
            curr_res = ""
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_res = s[l] + curr_res + s[r]
                l-=1
                r+=1
            if len(curr_res) > len(res):
                res = curr_res
        
        return res

