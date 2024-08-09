from collections import Counter

""" Sliding window. """
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # do through s2 in O(n) time?

        chars = Counter(s1)

        l, r = 0, 0

        while l <= r < len(s2):
            # case 1: right char in the string
            if s2[r] in chars and chars[s2[r]]:
                chars[s2[r]] -= 1
                r += 1

            # case 2: right char used too many times
            elif s2[r] in chars:
                while s2[l] != s2[r]:
                    chars[s2[l]] += 1
                    l += 1
                chars[s2[l]] += 1
                l += 1
            
            # case 3: right char not in the string
            else:
                # add all of the nums back to chars
                while l < r:
                    chars[s2[l]] += 1
                    l += 1
                r += 1
                l += 1
            
            print(l, r, chars)

            
            # return true if all of the chars are used
            if (r - l == len(s1)):
                return True
        
        return False
            




        