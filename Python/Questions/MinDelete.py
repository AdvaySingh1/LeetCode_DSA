from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """Determines the minimum number of intervals to delete

        Args:
            intervals (List[List[int]]): List of the intervals with a start and end value

        Returns:
            int: minimum number of intervals to delete without an overlapping interval
        """
        intervals.sort(key=lambda x: x[0])

        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prevEnd:
                prevEnd = min(prevEnd, end)
                res += 1
            else:
                prevEnd = end

        return res