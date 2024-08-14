#include <vector>
#include <string>

using namespace std;

// The following is an O(n) space implementation of quick sort

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
    void quickSortHelper(vector<Pair> &pairs, int start, int end)
    {
        if (start < end)
        {
            Pair &pivot = pairs[end];

            int left = start;
            for (int i = start; i < end; i++)
            {
                if (pairs[i].key <= pivot.key)
                {
                    swap(pairs[i], pairs[left++]);
                }
            }
            swap(pairs[left], pairs[end]);

            quickSortHelper(pairs, start, left - 1);
            quickSortHelper(pairs, left + 1, end);
        }
    }
    vector<Pair> quickSort(vector<Pair> &pairs)
    {
        quickSortHelper(pairs, 0, pairs.size() - 1);
        return pairs;
    }
};

/**
 * The following is the O(n) space implementation. Similar to MergeSort,
 * the n takes over the log(n) space of the stacks.
 *
 *
 * // Definition for a Pair
// class Pair {
// public:
//     int key;
//     string value;
//
//     Pair(int key, string value) : key(key), value(value) {}
// };
class Solution {
public:
    vector<Pair> quickSort(vector<Pair>& pairs) {
        if (pairs.size() == 0){
            vector<Pair> v;
            return v;
        }
        Pair pivot = pairs.back();
        size_t left = 0;

        for (size_t i = 0; i < pairs.size() - 1; i++){
            if (pairs[i].key < pivot.key){
                Pair tmp(pairs[i]);
                pairs[i] = pairs[left];
                pairs[left++] = tmp;
            }
        }

        pairs[pairs.size() - 1] = pairs[left]; // not stable
        pairs[left] = pivot;


        vector<Pair> res; vector<Pair> p;
        vector<Pair> a(pairs.begin(), pairs.begin() + left);
        vector<Pair> b(pairs.begin() + left + 1, pairs.end());


        res.reserve(pairs.size());


        a = quickSort(a);
        a.push_back(pivot);
        b = quickSort(b);

        res.insert(res.end(), a.begin(), a.end());
        res.insert(res.end(), b.begin(), b.end());

        return res;
    }
};

 */