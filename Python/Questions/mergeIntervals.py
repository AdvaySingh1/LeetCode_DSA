from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(n log n)
        intervals.sort(key=lambda x: x[0]) # sort based on times starting
        res = []

        for i in intervals:
            if res and i[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append([i[0], i[1]])
        return res
            