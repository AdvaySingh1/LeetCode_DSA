from collections import defaultdict
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        """ This is a O(n^3 + q) implementation """
        adj_l = {}
        for i in range(numCourses):
            adj_l[i] = []
        for u, v in prerequisites:
            adj_l[v].append(u)
    

        prereq = defaultdict(set)

        def dfs(crs: int) -> set:
            if crs not in prereq: # a form of dynamic programming
                prereq[crs] = set()
                for pre in adj_l[crs]:
                    prereq[crs].update(dfs(pre))
                    prereq[crs].add(pre)
            return prereq[crs]
        
        for i in range(numCourses):
            dfs(i)
        res = []

        for u, v in queries:
            res.append(u in prereq[v])
        return res

        # nomrmal dfs here

        """ The following is a brute force impl with O(q * n^2) """

        # create adj_l
        # adj_l = {}

        # for i in range(numCourses):
        #     adj_l[i] = []
        # for pre, post in prerequisites:
        #     adj_l[post].append(pre)
        
        # res = []

        # def dfs(dst, src):
        #     if src in visited:
        #         return False
        #     if src == dst:
        #         return True
            
        #     visited.add(src)
            
        #     for c in adj_l[src]:
        #         if dfs(dst, c):
        #             return True
            
        #     return False
        
        # for pre, post in queries:
        #     visited = set()
        #     res.append(dfs(pre, post))
        
        # return res