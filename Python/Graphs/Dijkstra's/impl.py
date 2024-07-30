from typing import List
from collections import defaultdict
from typing import Dict
import heapq

""" The following is an implementation of Dijkstra's algorithms.
    The adj_m initially created is of the form:
        src1: [[dst1, w1], [dst2, w2]], ..., [dstn, wn]
        src2: [[dst1, w1], [dst2, w2]], ..., [dstn, wn]
    Normal adj_m are of the form
        src1: [dst1, dst2, ..., dstn] 
        src2: [dst1, dst2, ..., dstn] 

    If there is no root found, then we return -1.
    Dijkstra's algorithm is a greedy algorithm; we always choose the next best step. Due to this,
    we naturally end up choosing the most efficient path first. However, due to the nature of the question,
    we are unable to simply stop the dfs loop when the res is the same length as n because not all 
    values within n are included in the edges. Some are disconnected regions and hence res will never be the same size.

    Time complexity discussion:
        The time complexity for creating adj_m:
            as we loop through each of the edges, with there being up to n - 1 edges for each vertex
            in the case of a fully connected graph, this operation is O(E) which is also the same thing as O(n^2).
            It's possible that none of the edges are connected, then this Ω(1).
        
        Time complexity for creating res:
            The DFS algorithm can have us visit each edge at most one time. Hence, a similar O(E) and Ω(1) logic applies.
            However, we do an additional step each of the time, the logarithmic addition or delition from the heap.
            Then we see a O(E * log(E)). However, we can re-write this as O(log ^ (V^2)) = O(E * 2 log (V)).
            Therefore, the formal time complexity if O(E * log(V)).
        
    The space complexity of O(E) or O(V^2) since we have to store each of the edges in the adj_m which is greater than O(V)
    which is needed for the res.
        """ 



class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        
        # create an adjcency matrix

        adj_m = defaultdict(list)

        for u, v, w in edges:
            adj_m[u].append((v, w))

        minHeap, res = [(0, src)], {}
        
        while minHeap:
            w, v = heapq.heappop(minHeap)
            if v not in res:
                res[v] = w
            
            for v2, w2 in adj_m[v]:
                if v2 not in res:
                    heapq.heappush(minHeap, (w2 + w, v2))
        
        for i in range(n):
            if i not in res:
                res[i] = -1
        
        return res




