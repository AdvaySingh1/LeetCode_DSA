class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # step one: determine the row

        t, b, row = 0, len(matrix) - 1, -1

        while (t <= b):
            m = t + ((b - t) // 2)
            if (matrix[m][len(matrix[m]) - 1] < target):
                t = m + 1
                print(t)
            elif (matrix[m][0] > target):
                b = m - 1
            else :
                row = m
                break

        if row < 0:
            return False
        
        l, r = 0, len(matrix[row]) - 1

        while (l <= r):
            m = l + ((r - l) // 2)
            if (matrix[row][m] < target):
                l = m + 1
            elif (matrix[row][m] > target):
                r = m - 1
            else:
                return True
    

        return False
        

