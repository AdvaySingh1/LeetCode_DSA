from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # return self.bruteForce(m, n, 0, 0)

        # grid = [[0 for col in range(n)] for row in range(m)]
        # return self.memorization(m, n, 0, 0, grid)

        return self.dp(m, n)

    """ The following is top-down apprach with O(m * n) space and O(2^(m * n)) for time """

    def bruteForce(self, m: int, n: int, r: int, c: int) -> int:
        if (r == m - 1 and c == n - 1):
            return 1
        
        elif (r >= m or c >= n):
            return 0
        
        else:
            return (self.bruteForce(m, n, r + 1, c) + self.bruteForce(m, n, r, c + 1))

    
    """ The following is top-down apprach with O(m * n) space and O(m * n) for time """

    def memorization(self, m: int, n: int, r: int, c: int, grid: List[List[int]]) -> int:
        if (r == m - 1 and c == n - 1):
            return 1

        elif (r >= m or c >= n):
            return 0

        elif grid[r][c] > 0:
            return grid[r][c]
        
        else:
            grid[r][c] = (self.memorization(m, n, r + 1, c, grid) 
            + self.memorization(m, n, r, c + 1, grid))
        
        return grid[r][c]

    """ The following in true bottom-up apprach with O(n) space and O(m * n) for time """
    
    def dp(self, m: int, n: int):
        prev_col = [0 for col in range(n)]

        for r in range(m - 1, -1, -1):
            curr_col = [0 for col in range(n)]
            curr_col[-1] = 1
            for c in range(n - 2, -1, -1):
                curr_col[c] = curr_col[c + 1] + prev_col[c]
            prev_col = curr_col
        
        return prev_col[0]

        
        