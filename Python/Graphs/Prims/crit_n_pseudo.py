import heapq
from collections import defaultdict
from typing import List


""" Prim's algorithm implementation """


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i) # (src, dst, w, i)
        
        adj_l = defaultdict(list) # O(E) space

        for v1, v2, w, i in edges: 
            adj_l[v1].append([v2, w, i])
            adj_l[v2].append([v1, w, i])

        # find the MST
        v1, _, _, _ = edges[0]
        heap, mst, visited = [(0, v1)], 0, set()

        while len(visited) < n and heap:
            w, v1 = heapq.heappop(heap)
            if v1 in visited:
                continue
            mst += w
            visited.add(v1)

            for n1, w2, _ in adj_l[v1]:
                if n1 not in visited:
                    heapq.heappush(heap, (w2, n1))

        critical, pseudo = [], []
        
        
        for v_1, v_2, w_, i in edges:
            v1, v2, _, _ = edges[0]
            heap, curr_mst, visited = [(0, v1, -1)], 0, set()

            while len(visited) < n and heap:
                w, v1, i_curr = heapq.heappop(heap)
                if v1 in visited or i_curr == i:
                    continue
                curr_mst += w
                visited.add(v1)

                for n1, w2, i_next in adj_l[v1]:
                    if n1 not in visited:
                        heapq.heappush(heap, (w2, n1, i_next))
                
            #print(i, curr_mst, len(visited))
            
            if (curr_mst != mst or len(visited) != n):
                critical.append(i)
                continue
            
            # determine if pseudo
            v1, v2, w_, i = edges[i]
            heap, curr_mst, visited = [(0, v2, -1)], w_, set()
            visited.add(v1)

            # need to add the edges which neighbor the already visited one
            for n1, w2, i_next in adj_l[v1]:
                    if n1 not in visited:
                        heapq.heappush(heap, (w2, n1, i_next))

            while len(visited) < n and heap:
                w, v1, _ = heapq.heappop(heap)
                if v1 in visited:
                    continue
                curr_mst += w
                visited.add(v1)

                for n1, w2, i_next in adj_l[v1]:
                    if n1 not in visited:
                        heapq.heappush(heap, (w2, n1, i_next))
            
            if (curr_mst == mst):
                pseudo.append(i)

            print(i, curr_mst)
        return [critical, pseudo]

        





