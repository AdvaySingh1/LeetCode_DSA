class Solution:
    def checkValidString(self, s: str) -> bool:
        """You are given a string s which contains only three types of characters: '(', ')' and '*'.

           Return true if s is valid, otherwise return false.

           A string is valid if it follows all of the following rules:

           Every left parenthesis '(' must have a corresponding right parenthesis ')'.
           Every right parenthesis ')' must have a corresponding left parenthesis '('.
           Left parenthesis '(' must go before the corresponding right parenthesis ')'.
           A '*' could be treated as a right parenthesis ')' character or a left parenthesis '(' character, or as an empty string "".
        Time: O(n).

        Args:
            s (str): The string in question.

        Returns:
            bool: Wether or not the string is valid.
        """
        leftMin, leftMax = 0, 0
        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0

        return leftMin == 0




        # O(n^3) solution
        # cache = {}
        # def dfs(i, n):
        #     if i == len(s):
        #         return n == 0
        #     if (i, n) in cache:
        #         return cache[(i, n)]
        #     if s[i] == "(":
        #         cache[(i, n)] = dfs(i + 1, n + 1)
        #     elif s[i] == "*":
        #         cache[(i, n)] = dfs(i + 1, n) or dfs(i + 1, n - 1) or dfs(i + 1, n + 1)
        #     else:
        #         cache[(i, n)] = dfs(i + 1, n - 1)
        #     return cache[(i, n)]
        
        # return dfs(0, 0)



        # choices = 0
        # stack = []

        # for c in s:
        #     if c == "*":
        #         choices += 1
        #     elif c == "(":
        #         stack.append(c)
        #     elif c == ")":
        #         if stack and stack[-1] == "(":
        #             stack.pop()
        #         else:
        #             choices -= 1
        #     if choices < 0:
        #         return False
        
        # return choices >= len(stack)
