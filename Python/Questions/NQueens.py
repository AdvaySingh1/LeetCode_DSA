from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """ N queens O(n!) solution. O(n^2) space solution. As the tree gets larger (n), the number of options began to decrease hence O(n!)

        Args:
            n (int): The size of the chess board.

        Returns:
            List[List[str]]: Valid possible solutions to the board.
        """
        res, board = [], [["."] * n for i in range(n)]
        def backtrack(r, vert, rightDiag, leftDiag):
            if r == n:
                copy = ["".join(col) for col in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c not in vert and r - c not in rightDiag and r + c not in leftDiag:
                    board[r][c] = "Q"
                    vert.add(c)
                    rightDiag.add(r-c)
                    leftDiag.add(r+c)
                    backtrack(r + 1, vert, rightDiag, leftDiag)

                    board[r][c] = "."
                    vert.remove(c)
                    rightDiag.remove(r-c)
                    leftDiag.remove(r+c)
            
        backtrack(0, set(), set(), set())
        return res

        # res = []
        # def dfs(i, pos, invalid):
        #     if i == n:
        #         res.append(pos.copy())
        #         return 
            
        #     for j in range(n):
        #         if (i, j) not in invalid:
        #             newInvalid = invalid.copy()
        #             # add vals to invalid

        #             # add vertical cols
        #             for r in range(i + 1, n):
        #                 newInvalid.add((r, j))
        #             # add diagonals
        #             for d in range(1, n):
        #                 newInvalid.add((i + d, j + d))
        #                 newInvalid.add((i + d, j - d))

        #             pos.append(f'{"." * j}Q{"." * (n - j - 1)}')
        #             dfs(i + 1, pos, newInvalid)
        #             pos.pop()
        
        # dfs(0, [], set())
        # return res



        