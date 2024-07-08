from typing import List
from collections import deque

"""
Time complexity if O(N * M) because we go through the matrix multiple times.
Space complexity if O(N * M) because we append each of the edges (parts of the matrix) to the queue potentially. 
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue, rows, cols = deque(), len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))

        

        def bfs() -> int:
            count = -1
            while len(queue) > 0:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                

                    neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                    for dr, dc in neighbors:
                        rr, cc = dr + r, dc + c
                        if (rr in range(rows) and cc in range(cols)
                            and grid[rr][cc] == 1):
                            queue.append((rr, cc))
                            grid[rr][cc] = 2
                count += 1
            
            return count
        

        
        
        count = bfs()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        
        return max(count, 0)
        


        

        