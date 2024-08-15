#include <vector>
using namespace std;


class Solution
{
public:
/**
 * @brief Binary O(lon(n)) Search
 * 
 * @param nums (vector<int>)
 * @param target 
 * @return int 
 */
    int search(vector<int> &nums, int target)
    {
        int l = 0;
        int r = nums.size() - 1;

        while (l <= r)
        {
            int m = l + (((r - l) / 2)); // to prevent integer overflow if both r and l are close to the limir
            if (nums[m] < target)
            {
                l = m + 1;
            }
            else if (nums[m] > target)
            {
                r = m - 1;
            }
            else
            {
                return m;
            }
        }
        return -1;
    }
};
