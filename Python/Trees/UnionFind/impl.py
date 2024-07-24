

""" The following is a union find. It is useful when determining is parts of a graph are connected 
    Due to the optimiations, the time complexity for the find (the bottleneck operation) reduces to O(1).
    More on this here: https://www.geeksforgeeks.org/union-by-rank-and-path-compression-in-union-find-algorithm/"""

""" Although the rank is temporarly altered after the find funciton, it's still accurate at the time of the union """


class UnionFind:
    
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}
        self.num_comp = n

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        # here we do path compression. How does this impact the rank? It becomes arbitrary.
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        xp, yp = self.find(x), self.find(y)
        if (xp == yp):
            return False

        if self.rank[xp] > self.rank[yp]:
            self.par[yp] = xp
        
        elif self.rank[xp] < self.rank[yp]:
            self.par[xp] = yp

        else:
            self.par[yp] = xp
            self.rank[xp] = 1
        self.num_comp -= 1
        return True

    def getNumComponents(self) -> int:
        return self.num_comp

