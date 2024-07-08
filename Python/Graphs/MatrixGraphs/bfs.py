from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        queue.append((0, 0))

        def is_valid(r, c, visited):
            return (r < len(grid) and c < len(grid[0])
                    and r >= 0 and c >= 0 and (r, c) not in visited
                    and grid[r][c] == 0)
        
        def is_end(r, c):
            return r == len(grid) - 1 and c == len(grid[0]) - 1


        path = 0
        while len(queue) > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if is_valid(r, c, visited):
                    queue.append((r + 1, c))
                    queue.append((r, c + 1))
                
                    visited.add((r, c))

                    if is_end(r, c):
                        return path

            path += 1
            

        
        return -1