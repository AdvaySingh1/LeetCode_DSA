from typing import List
import heapq

""" The brute force solution to this algorithm would be O(3^V). However, this greedy apprach is only O(V^2 log(v))."""


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        i, j, t, n = 0, 0, 0, len(grid)

        # make a list to get to the bottom right value

        heap = [(grid[i][j], i, j)]
        visited = set()
        

        while i != n - 1 or j != n - 1:
            curr_e, i, j = heapq.heappop(heap)
            visited.add((i, j))
            print(i, j)
            t = max(t, curr_e)



            neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for di, dj in neighbors:
                i2, j2 = i + di, j + dj
                if (i2 in range(n) and j2 in range(n) and 
                    (i2, j2) not in visited):
                
                    heapq.heappush(heap, (grid[i2][j2], i2, j2))

    
        return max(t, grid[n - 1][n - 1])