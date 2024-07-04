#include <vector>
using namespace std;

class Solution
{
public:
    bool searchMatrix(vector<vector<int>> &matrix, int target)
    {
        int r = matrix[0].size() - 1;
        int l = 0;

        int t = 0;
        int b = matrix.size() - 1;
        int row = -1;

        while (t <= b)
        {
            int m = t + ((b - t) / 2);
            if (matrix[m][r] < target)
            {
                t = m + 1;
            }
            else if (matrix[m][0] > target)
            {
                b = m - 1;
            }
            else
            {
                row = m;
                break;
            }
        }

        if (row < 0)
            return false;

        while (l <= r)
        {
            int m = l + ((r - l) / 2);
            if (matrix[row][m] < target)
            {
                l = m + 1;
            }
            else if (matrix[row][m] > target)
            {
                r = m - 1;
            }
            else
            {
                return true;
            }
        }

        return false;
    }
};
