import heapq

""" The following is the kruskal's algorithm which is also used to fint eh minimum spanning tree.
    Space complexity if the heap which can have all of the edges and hence O(E) or O(V^2).
    The time complexity is O(E log(V)) because for each of the edges, we are doing a heap operation.
"""

class UnionFind:
    def __init__ (self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x) -> int:
        if self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
        return self.par[x]

    def union(self, a, b) -> bool:
        pa, pb = self.find(a), self.find(b)
        
        if pa == pb:
            return False
        
        if self.rank[pa] > self.rank[pb]:
            self.par[pb] = pa
        elif self.rank[pa] < self.rank[pb]:
            self.par[pa] = pb
        else:
            self.par[pb] = pa
            self.rank[pa] += 1
        return True
        



class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        heap = []
        u = UnionFind(n)
        res = 0
        e = 0

        for v1, v2, w in edges:
            heapq.heappush(heap, (w, v1, v2))
        
        while heap:
            w, v1, v2 = heapq.heappop(heap)
            if u.union(v1, v2):
                e += 1
                res += w
        
        return res if e == n - 1 else -1