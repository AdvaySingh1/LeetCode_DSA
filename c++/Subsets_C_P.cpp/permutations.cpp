#include <vector>
using namespace std;
/**
 * Refer to Python version for discussion on time complexity O(n * n!)
 */

// using namespace name
// {

// } // namespace name

class Solution
{
public:
    vector<vector<int>> permute(vector<int> &nums)
    {

        vector<vector<int>> res;

        if (nums.empty())
        {
            res.push_back({});
            return res;
        }

        int val = nums.back();
        nums.pop_back(); // back for O(1) although this is overpowered

        vector<vector<int>> perms = permute(nums);

        for (const vector<int> &perm : perms)
        {
            for (size_t i = 0; i <= perm.size(); i++)
            {
                vector<int> newPerm(perm);
                newPerm.insert(newPerm.begin() + i, val);
                res.push_back(newPerm);
            }
        }

        nums.push_back(val);

        return res;
    }
};
