from typing import List
from collections import defaultdict
import heapq


"""
    The following has a similar time and space complexity to Dijkstra's at O(E) space and O(E * log(V)) time.
"""

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        
        # create the adj_m O(E) time and space

        adj_m = defaultdict(list)

        for v1, v2, w in edges:
            adj_m[v1].append((v2, w))
            adj_m[v2].append((v1, w))
        
        heap = [[0, 0]] # arbitrarly choosing an edge. Can be edges[0][0]
        visited = set()
        res = 0

        while heap and len(visited) < n: #if making a list, the condidion is while the length of the list is not the same as edges
            w, v = heapq.heappop(heap)
            if v in visited:
                continue
            visited.add(v)
            res += w

            for v2, w2 in adj_m[v]:
                if v2 not in visited:
                    heapq.heappush(heap, (w2, v2))

        
        return res if len(visited) == n else -1

