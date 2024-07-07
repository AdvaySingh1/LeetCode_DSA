from typing import List

class Solution:
    """ Count paths implementation. 
        Time complexity: O(4 ^(N * M)). N and M are the dimensions of the matrix respectivly. Consider this a tree with 4 possible routes which are potential the length of the entire matrix.
        Space complexity: O(N * M). This is because we are keeping track of the visited which is potentially the size of the entire matrix."""


    def countPaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = dict()


        def _helper(grid, visited, r, c):

            def isOutOfBounds() -> bool:
                if (r < 0 or c < 0
                    or r >= rows or c >= cols
                    or (r, c) in visited
                    or grid[r][c] == 1):
                    return True


            def reachedEnd() -> bool:
                if ( r == rows - 1
                    and c == cols - 1):
                    return 1


            if (isOutOfBounds()):
                return 0
            
            elif (reachedEnd()):
                return 1

            
            visited[(r, c)] = 0

            count = 0
            count += _helper(grid, visited, r + 1, c)
            count += _helper(grid, visited, r - 1, c)
            count += _helper(grid, visited, r, c + 1)
            count += _helper(grid, visited, r, c - 1)

            visited.pop((r, c))

            return count

        

        return _helper(grid, visited, 0, 0)