from collections import deque
from typing import List


"""
BFS and DFS apprach. Idea in each is to created a visited set. 

BFS
Time complexity is O((N*M)^2) because in each iteration, we are potentially going through the rest of the islands.
Space complexity if O(N * M) because we are creating queue and visited (set of touples) structures.

DFS
Time complexity is O((N*M)^2) because in each iteration, we are potentially going through the rest of the islands.
Space complexity if O(N * M) because we are creating visited (set of touples) structure and the call stack for the dfs recursion.

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # using bfs
        visited = set()
        count, rows, cols = 0, (len(grid)), (len(grid[0]))


        # def bfs(r, c) -> int:
        #     queue = deque()
        #     queue.append((r, c))
            
        #     while queue:
        #         for i in range(len(queue)):
        #             r, c = queue.popleft()

        #             if (r, c) not in visited:

        #                 neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        #                 for dr, dc in neighbors:
        #                     if (r + dr in range(rows) and c + dc in range(cols)
        #                         and grid[r + dr][c + dc] == "1"):
        #                         queue.append((r + dr, c + dc))
                    
        #                 visited.add((r, c))

        def dfs(r, c) -> None:
            if (grid[r][c] == '0'
                or (r, c) in visited):
                return
                

            neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in neighbors:
                if r + dr in range(rows) and c + dc in range(cols):
                    dfs(r + dr, c + dc)
                
                visited.add((r, c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    dfs(r, c)
        

        return count
    


    """
    The following is an implementation of the largest island both in DFS and BFS.
    It adheres to a similar space and time complexity as the previous solution.
    """


    class Solution2:
        def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
            maxArea, rows, cols = 0, len(grid), len(grid[0])

            visited = set()

            # def dfs(r, c) -> int:

            #     if (r, c) in visited or grid[r][c] == 0:
            #         return 0
                
            #     visited.add((r, c))
                
            #     neighbors, count = [[1, 0], [-1, 0], [0, 1], [0, -1]], 1
            #     for dr, dc in neighbors:
            #         if r + dr in range(rows) and c + dc in range(cols):
            #             count += dfs(r + dr, c + dc)

            #     return count

            def bfs(r, c)-> int:
                queue, count = deque(), 1
                queue.append((r, c))
                visited.add((r, c))

                while (len(queue) > 0):
                    
                    for i in range(len(queue)):

                        r, c = queue.popleft()
                        

                        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                        for dr, dc in neighbors:
                            if (dr + r in range(rows) and dc + c in range(cols)
                                and grid[r + dr][c + dc] == 1 
                                and (r + dr, c + dc) not in visited):
                                count += 1
                                queue.append((r + dr, c + dc))
                                visited.add((r + dr, c + dc))
                
                return count




            for r in range(rows):
                for c in range(cols):
                    if (r, c) not in visited and grid[r][c] == 1:
                        maxArea = max(maxArea, bfs(r, c))
        
            return maxArea
