from typing import List

"""
    Time and space complexity.
        Initializing the adjacency list takes (O(V)) time since you're iterating over all vertices. (This is done within DFS for c++).
        Building the adjacency list from edges takes (O(E)) time since you're iterating over all edges.
        The DFS function, when called for each vertex, will visit each vertex and each edge exactly once, leading to (O(V + E)) time.
    Hence O(V + E).


    Space complexity:
        Adjacency List: Requires (O(V + E)) space.
        Visited and Path Sets: Each can grow up to (O(V)) space.
        Result List: Will store all vertices, so it requires (O(V)) space.
        Recursion Stack: In the worst case, the depth of the recursion stack can be (O(V)).
    Hence O(V + E).
"""


class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        # create adj list O(E) space and time
        adj_l = {}

        for i in range(n):
            adj_l[i] = []

        for src, dst in edges:
            adj_l[src].append(dst)

        res, visited, path, = [], set(), set()

        def dfs(src: int) -> bool:
            if src in path: # used fro cycle detection
                return False
            if src in visited:
                return True

            path.add(src)
            visited.add(src)
            for n in adj_l[src]:
                if not dfs(n):
                    return False

            path.remove(src)
            res.append(src)

            return True

        
        for i in range(n):
            if not dfs(i):
                return []
        
        res.reverse()
        return res
        


