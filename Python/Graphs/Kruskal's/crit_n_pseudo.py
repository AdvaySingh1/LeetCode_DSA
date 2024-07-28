class UnionTree:
    def __init__ (self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, a: int, b: int) -> bool:
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        
        if self.rank[pa] > self.rank[pb]:
            self.par[pb] = pa
            self.rank[pa] += self.rank[pb]
        elif self.rank[pa] < self.rank[pb]:
            self.par[pa] = pb
            self.rank[pb] += self.rank[pa]
        else:
            self.par[pb] = pa
            self.rank[pa] *= 2
        
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i) # (v1, v2, w, i)
        
        edges.sort(key=lambda edge: edge[2]) # same as using the heap

        u = UnionTree(n)
        mst = 0
        for v1, v2, w, _ in edges:
            if u.union(v1, v2):
                mst += w
        
        critical, pseudo = [], []

        for v_1, v_2, w_, i in edges:
            uf, curr_mst = UnionTree(n), 0
            for v1, v2, w, i2 in edges:
                if i != i2 and uf.union(v1, v2):
                    curr_mst += w

            if max(uf.rank) < n or curr_mst > mst:
                critical.append(i)
                continue
            
            uf = UnionTree(n)
            uf.union(v_1, v_2)
            curr_mst = w_
            for v1, v2, w, _ in edges:
                if uf.union(v1, v2):
                    curr_mst += w
            
            if curr_mst == mst:
                pseudo.append(i)
            
        return [critical, pseudo]




