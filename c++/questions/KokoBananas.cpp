#include <vector>
using namespace std;

// note that h has to be greater than the number of piles. Hence, the max k can be is the max element of the piles.

class Solution
{
public:
    int minEatingSpeed(vector<int> &piles, int h)
    {
        int l = 1, r = *max_element(piles.begin(), piles.end()), res = 0; // because hours is greater than or equal to piles

        while (l <= r)
        {
            int hours = 0;
            int k = l + ((r - l) / 2);

            for (auto pile : piles)
            {
                hours += ceil((double)pile / k);
            }

            if (hours > h)
            {
                l = k + 1;
            }
            else
            {
                res = k;
                r = k - 1;
            }
        }
        return res;
    }
};
