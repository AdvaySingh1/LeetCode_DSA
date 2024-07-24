/**
 * Duplicate subsets
 *
 * The time complexity comes from copying the leaf nodes and it's n 2^n because at each step, there are two decisions and therefore 2^n
 */

#include <vector>

using namespace std;

class Solution
{
public:
    vector<vector<int>> subsetsWithDup(vector<int> &nums)
    {
        vector<int> vals;
        sort(nums.begin(), nums.end());
        subsetsHelper(vals, nums, 0);

        return res;
    }

    void subsetsHelper(vector<int> &vals, vector<int> &nums, int i)
    {
        if (i >= nums.size())
        {
            res.push_back(vals); // this is the O(n) operation at only the leaf nodes
            return;
        }

        vals.push_back(nums[i]);
        subsetsHelper(vals, nums, i + 1);
        vals.pop_back();

        while (i + 1 < nums.size() && nums[i + 1] == nums[i])
        {
            i++;
        }
        subsetsHelper(vals, nums, i + 1);
    }

private:
    vector<vector<int>> res;
};
