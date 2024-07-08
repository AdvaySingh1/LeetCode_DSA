from collections import deque
from typing import Optional

""" The following is an implemention of an adjacency list.
    Time complecity for hasPath
        BFS:
            Time complexity: O(V + E) where E < V^2. This is since we are going thorugh the queue one time.
            Space complexity: O(V + E) due to the queue.
        DFS:
            Time complexity: O(V^E) because at each V, we have the option for all of it's neighbors.
            Space complexity: O(V + E) due to the call stack.
            """


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if dst not in self.graph:
            self.graph[dst] = set()
        if src not in self.graph:
            self.graph[src] = set()

        if dst not in self.graph[src]:
            self.graph[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.graph:
            if dst in self.graph[src]:
                self.graph[src].remove(dst)
                return True
        
        return False

    def hasPath(self, src: int, dst: int) -> bool:

        visited = set()
        
        # def dfs(s, visited) -> bool:
        #     if s == dst:
        #         return True
        #     hasPath = False
        #     visited.add(s)
        #     for d in self.graph[s]:
        #         if d not in visited:
        #             hasPath = hasPath or dfs(d, visited)
        #     visited.remove(s)

        #     return hasPath

        def bfs(s, visited):
            queue = deque()
            queue.append(s)

            while (len(queue)) > 0:
                for i in range(len(queue)):
                    sr = queue.popleft()

                    for d in self.graph[sr]:
                        if d not in visited:
                            queue.append(d)
                            visited.add(sr)
                        if d == dst:
                            return True
            
            return False


        return bfs(src, visited)
    

    """
    O (V + E) time using a similar old to new hashmap
    O (v + E) space.
    """


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(n):
            if n in oldToNew:
                return oldToNew[n]
            
            copy = Node(n.val)
            oldToNew[n] = copy
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        return dfs(node) if node else None



        


