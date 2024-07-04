#include <vector>
#include <algorithm>
#include <queue>

using namespace std;
/**
 * Approach one. Min heap:
 */

class Solution
{
public:
    int findKthLargest(vector<int> &nums, int k)
    {
        priority_queue<int, std::vector<int>, greater<int>> min_heap(nums.begin(), nums.begin() + k);

        for (int i = k; i < nums.size(); i++)
        {
            if (nums[i] > min_heap.top())
            {
                min_heap.pop();
                min_heap.push(nums[i]);
            }
        }

        return min_heap.top();
    }
};

/**
 * Approach two partition and quickselect
 */

/**
 * class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {

        int start = 0; int end = nums.size() - 1;
        k = nums.size() - k;

        while (start < end){
            int pivot = partition(nums, start, end);

            if (pivot < k){
                start = pivot + 1;
            } else if (pivot > k){
                end = pivot - 1;
            } else {
                break;
            }
        }

        return nums[k];

    }

    int partition(vector<int>& nums, int start, int end){
        int j = start; int pivot = nums[end];
        for (int i = start; i < end; i++){
            if (nums[i] < pivot){
                swap(nums[i], nums[j++]);
            }
        }
        swap(nums[j], nums[end]);
        return j;
    }
};

 */