import heapq
from collections import defaultdict
from typing import List


""" The time complexity of this implmentation is O(E log V) or O(V^2 log V) where V is all of the points. O(E) space. """


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # firstly create a complete graph O(V^2) space and time.

        

        adj_l = defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                m_d = abs(x2 - x1) + abs(y2 - y1)

                adj_l[i].append((j, m_d))
                adj_l[j].append((i, m_d))
        
        print(adj_l)

        m_h = [(0, 0)]
        visited = set()
        res = 0

        while(len(visited) < len(adj_l)):
            w, v = heapq.heappop(m_h)
            if v not in visited:
                visited.add(v)
                res += w

                for v2, w2 in adj_l[v]:
                    if v2 not in visited:
                        heapq.heappush(m_h, (w2, v2))
            

        return res