#include <unordered_set>
#include <set>

using namespace std;

class Solution
{
public:
    int longestConsecutive(vector<int> &nums)
    {
        unordered_set<int> s; // using hasing, this leads to best case of O(n) best case and O(n^2) word case when theres collisions. Chaining in this case and optimizations to prevent collisions in the std lib.
        // set<int> s; This approach would lead to a O(n log n) because finding elements is O(log n) for a set which is ordered and implemented on a BST

        for (int n : nums)
        {
            s.insert(n);
        }

        int max_count = 0;

        for (int n : s)
        {
            if (s.find(n - 1) == s.end())
            {
                int large = n, count = 0;
                while (s.find(large) != s.end())
                {
                    large++;
                    count++;
                }
                max_count = max(max_count, count);
            }
        }
        return max_count;
    }
};
