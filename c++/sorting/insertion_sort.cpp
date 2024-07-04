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

// make a copy of the vector each time

class Solution
{
public:
    vector<vector<Pair>> insertionSort(vector<Pair> &pairs)
    {
        vector<vector<Pair>> res;
        for (int i = 0; i < pairs.size(); i++)
        {
            int p = i;
            while ((p > 0) && (pairs[p].key < pairs[p - 1].key))
            {
                Pair temp = pairs[p]; // assuming overloaded param
                pairs[p] = pairs[p - 1];
                pairs[p - 1] = temp;
                p--;
            }
            res.push_back(pairs); // not an array hence not a pointer. This object is later printed.
        }
        return res;
    }
};