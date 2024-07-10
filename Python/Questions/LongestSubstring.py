class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # return self.bruteForce(text1, text2)
        
        grid = [[0 for i in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for r in range(len(grid) - 2, -1, -1):
            for c in range(len(grid[0]) - 2, -1, -1):
                if text1[r] == text2[c]:
                    grid[r][c] = 1 + grid[r + 1][c + 1]
                else:
                    grid[r][c] = max(grid[r + 1][c], grid[r][c + 1])
        
        return grid[0][0]


    
    def bruteForce(self, text1: str, text2: str):
        if not text1 or not text2:
            return 0

        if text1[0] == text2[0]:
            return 1 + self.bruteForce(text1[1:], text2[1:])
        else:
            return max(self.bruteForce(text1[1:], text2), self.bruteForce(text1, text2[1:]))
