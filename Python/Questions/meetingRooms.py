from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here

        if not intervals:
            return 0
        
        s, e = [], []
        for meeting in intervals:
            s.append(meeting.start)
            e.append(meeting.end)
        
        s.sort()
        e.sort()

        rooms = 1
        count, j, i = 0, 0, 0
        while i < len(s): # only need to increment the start ones
            if s[i] < e[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            rooms = max(rooms, count)

        return rooms