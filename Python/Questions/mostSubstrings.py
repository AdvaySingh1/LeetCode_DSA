from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """You are given a string s consisting of lowercase english letters. We want to split the string into as many substrings as possible, while ensuring that each letter appears in at most one substring. 

        Args:
            s (str): input string

        Returns:
            List[int]: a list of integers representing the size of these substrings in the order they appear in the string.
        """
        # create a hashmap of the last index O(n) solution
        lastIndex = {}
        for i in range(len(s)):
            lastIndex[s[i]] = i
        res = []
        i = 0
        while i < len(s):
            start_index = i - 1
            curr_last_index = lastIndex[s[i]]
            while i <= curr_last_index:
                curr_last_index = max(curr_last_index, lastIndex[s[i]])
                i += 1
            res.append(curr_last_index - start_index)
        return res

        # brute Force O(n^2) solution
        # res = []
        # i = 0
        # while i < len(s):
        #     n = i
        #     charsToI = set()
        #     charsToI.add(s[i])
        #     for p in range(i + 1, len(s)):
        #         if s[p] in charsToI:
        #             for c in s[i+1: p+1]:
        #                 charsToI.add(c)
        #             n = p
        #     res.append(n - i + 1)
        #     i = n + 1
        # return res




