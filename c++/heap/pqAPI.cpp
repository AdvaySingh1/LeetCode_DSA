/**
 * Note that this is not the best way to solve this question. The priority queue doen't provide a heapidy API therefore, 
 * the time complexity is O(nlogn). However, quick select can accomplish this in O(n) time. However, finding the elemnt everytime still provides
 * a reason to stick with the heapify tactic since that's only O(logn)
 */

#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

class KthLargest
{
public:
    KthLargest(int k_in, vector<int> &nums) : k(k_in)
    {
        for (int num : nums)
        {
            minHeap.push(num);
            if (minHeap.size() > k)
            {
                minHeap.pop();
            }
        }
    }

    int add(int val)
    {
        minHeap.push(val);
        if (minHeap.size() > k)
        {
            minHeap.pop();
        }
        return minHeap.top();
    }

private:
    priority_queue<int, vector<int>, greater<int>> minHeap; // check api
    int k;
};
