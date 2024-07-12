fr
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # return self.bruteForce(obstacleGrid, 0, 0)
        # cache = [[0 for i in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
        # return self.memorization(obstacleGrid, 0, 0, cache)
        return self.df(obstacleGrid, 0, 0)
    
    def bruteForce(self, grid: List[List[int]], m: int, n):
        if (m >= len(grid) or n >= len(grid[0]) or grid[m][n] == 1):
            return 0
        elif (m == len(grid) - 1 and n == len(grid[0]) - 1):
            return 1
        
        else:
            return self.bruteForce(grid, m + 1, n) + self.bruteForce(grid, m, n + 1)
        
    
    def memorization(self, grid: List[List[int]], m: int, n: int, cache: List[List[int]]):
        if (m >= len(grid) or n >= len(grid[0]) or grid[m][n] == 1):
            return 0

        elif (m == len(grid) - 1 and n == len(grid[0]) - 1):
            return 1

        elif (cache[m][n] > 0):
            return cache[m][n]
        
        else:
            cache[m][n] = (self.memorization(grid, m + 1, n, cache)
                            + self.memorization(grid, m, n + 1, cache))
        
        return cache[m][n]

    def df(self, grid: List[List[int]], m: int, n: int):
        prev_row = [0 for i in range(len(grid[0]))]

        for r in range(len(grid) - 1, -1, -1):
            curr_row = [0 for i in range(len(grid[0]))]
            curr_row[-1] = 0
            curr_row[-1] = 0 if grid[r][-1] == 1 or (r < len(grid) - 1 and prev_row[-1] == 0) else 1
            for c in range(len(grid[0]) - 2, -1, -1):
                curr_row[c] = (prev_row[c] + curr_row[c + 1]) if grid[r][c] == 0 else 0
            prev_row = curr_row
        
        return prev_row[0]
                    

