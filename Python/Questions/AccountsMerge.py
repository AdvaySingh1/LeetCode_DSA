
from typing import DefaultDict
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
    def find(self, x: str) -> str:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x: str, y: str) -> bool:
        xp, yp = self.find(x), self.find(y)
        if (xp == yp):
            return False
        if (self.rank[xp] > self.rank[yp]):
            self.par[yp] = xp
            self.rank[xp] += self.rank[yp]
        else:
            self.par[xp] = yp
            self.rank[yp] += self.rank[xp]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        uf = UnionFind(len(accounts))
        iToA = {}

        for i, a in enumerate(accounts):
            for email in a[1:]: # O(n) space where n is the average size of the emails (less than the total)
                if email in iToA:
                    uf.union(i, iToA[email])
                else:
                    iToA[email] = i
        
        # make a leader dict now
        emailGroup = defaultdict(list)
        for email, i in iToA.items():
            leader = uf.find(i)
            emailGroup[leader].append(email)
        
        res = []
        for i, emails in emailGroup.items():
            res.append([accounts[i][0]] + sorted(emails))
        return res
        
