from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """Given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

        Args:
            n (int): number of each side of parenthesis

        Returns:
            List[str]: all the well formed parenthesis
        """
        res = []
        def backTrack(s, r, i):
            if r > n:
                return
            if r < 0:
                return
            if i == n * 2:
                if r == 0:
                    res.append(s)
                return
            backTrack(s + "(", r + 1, i + 1)
            backTrack(s + ")", r - 1, i + 1)

        
        backTrack("", 0, 0)
        return res
        