#include <vector>

using namespace std;

class Solution {
public:
/**
 * @brief 
 * 
 * @param nums 
 * @param target 
 * @return int 
 */
    int search(vector<int>& nums, int target) {
        // first find the min

        int l = 0, r = nums.size() - 1, m = nums.size() / 2;
        while (l <= r){
            if (nums[m] == target) return m;
            if (nums[m] > target){
                if (nums[l] <= target){
                    r = m - 1;
                } else { // here
                    if (nums[m] > nums[r]){
                        l = m + 1;
                    } else {
                        r = m - 1;
                    }
                }
            } else {
                if (nums[r] >= target){
                    l = m + 1;
                } else { // here 
                    if (nums[m] > nums[l]){
                        l = m + 1;
                    } else {
                        r = m - 1;
                    }
                }
            }
            m = l + ((r - l) / 2); // prevent int overflow
        }
        return-1;

        /* O(n) solution */
        // int res = 0;
        // for (vector<int>::iterator i = nums.begin(); i != nums.end(); i++, res++){
        //     if (*i == target) return res;
        // }
        // return -1;
    }
};
