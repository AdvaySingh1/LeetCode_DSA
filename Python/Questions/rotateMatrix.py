from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.

           You must rotate the matrix in-place. Do not allocate another 2D matrix and do the rotation.

        Args:
            matrix (List[List[int]]): image represented as 2-D grid.
        """

        # transpose = [[matrix[j][i] for j in range(n)] for i in range(n)]

        # if can make matrix copy O(n^2) space
        # new_matrix = [[matrix[i][j] for j in range(n)] for i in range(n)]

        # for i in range(n):
        #     for j in range(n):
        #         matrix[i][j] = new_matrix[n - j - 1][i]

        l, r = 0, len(matrix) - 1

        while (l < r):
            for i in range(r-l):
                t, b = l, r

                # store the value at the top left
                top_left = matrix[t][l + i]

                # insert bottom left to top left
                matrix[t][l + i] = matrix[b - i][l]

                # insert bottom right to bottom left
                matrix[b - i][l] = matrix[b][r - i]

                # insert the top right to the bottom right
                matrix[b][r - i] = matrix[t + i][r]

                # insert the top left to the top right
                matrix[t + i][r] = top_left

            l, r = l + 1, r - 1



        

