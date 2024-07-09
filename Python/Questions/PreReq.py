from typing import List

""" Prerequisites implementaiton (make a graph for all of the classes and see if they are eligigible)
    Time complexity: O((N * M)^N) since for each node we will check each of it's connections
    Space complexity: O(N * M) for the graph we create.
    """
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for pre, crs in prerequisites:
            graph[pre].append(crs)

        visited = set()

        def dfs(pre):
            if pre in visited:
                return False
            
            visited.add(pre)
            for nex in graph[pre]:
                if not dfs(nex):
                    return False
            
            visited.remove(pre)
            
            return True


        for pre, crs in prerequisites:
            if not dfs(pre):
                return False
        
        return True


        


        

        
        