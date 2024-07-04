#include <vector>
#include <string>
using namespace std;
// Definition for a Pair
class Pair {
public:
    int key;
    string value;

    Pair(int key, string value) : key(key), value(value) {}
};

class Solution
{
public:
    vector<Pair> mergeSort(vector<Pair> &pairs)
    {
        // base case
        if (pairs.size() <= 1)
        {
            return pairs;
        }

        size_t mid = pairs.size() / 2;
        vector<Pair> arr1(pairs.begin(), pairs.begin() + mid);
        vector<Pair> arr2(pairs.begin() + mid, pairs.end());

        // recurse on both the segments
        vector<Pair> res1 = mergeSort(arr1);
        vector<Pair> res2 = mergeSort(arr2);

        // filter the two sorted arrays
        vector<Pair> res;
        res.reserve(pairs.size()); // reserve space to avoid relocation for better T
        auto it1 = res1.begin();
        auto it2 = res2.begin();

        while (it1 != res1.end() && it2 != res2.end())
        {
            if (it1->key <= it2->key)
            {
                res.push_back(*it1++);
            }
            else
            {
                res.push_back(*it2++);
            }
        }

        res.insert(res.end(), it1, res1.end()); // position, it1, it2 when inserting from something else
        res.insert(res.end(), it2, res2.end());

        return res;
    }
};
