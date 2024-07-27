from typing import List


""" Time complexity is n * 3.2 ^ n"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        nToC = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}

        res = []
        subset = []

        if not digits:
            return res


        def lCHelper(i: int, subset):
            if i == len(digits):
                res.append("".join(subset))
                return
            
            for c in nToC[int(digits[i])]:
                subset.append(c)
                lCHelper(i + 1, subset)
                subset.pop()
            
        lCHelper(0, subset)

        return res
    

"""This is a 3.k^n solution."""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        nToC = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}

        res = []

        def lCHelper(i: int, subset):
            if i == len(digits):
                res.append(subset)
                return
            
            for c in nToC[int(digits[i])]:
                lCHelper(i + 1, subset + c)
        

        if digits:
            lCHelper(0, "")

        return res





