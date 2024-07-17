#include <functional> // lambda functions
#include <vector>
#include <algorithm> // for the heap (not a container but and algorithms like the std::sort)
#include <iostream>

using namespace std;

/**
 * Documentation for heap algorithms: https://www.geeksforgeeks.org/cpp-stl-heap/
 * The following is an implementation of two heaps for finding the min value in a stream of numbers.
    Brute force apprach: sort the seqeunce every time and return the median everytime.
     - This would be a O(n^2 log(n)) big omega approach if using mergesort and a O(n^3) big O approach if using quick sort.
    Our approach: using two different heaps. A small max heap and a large min heap
 */

class MedianFinder
{
public:
    MedianFinder() {}

    void addNum(int num)
    {
        if (large.size() > 0 && num > large.front())
        {
            large.push_back(num);
            push_heap(large.begin(), large.end(), minComp);
        }
        else
        {
            small.push_back(num);
            push_heap(small.begin(), small.end(), maxComp);
        }

        if (small.size() > large.size() + 1)
        {
            int largest_small_val = small.front();
            pop_heap(small.begin(), small.end(), maxComp); // move largest to the back
            small.pop_back();
            // add the largest val to the large heap
            large.push_back(largest_small_val);
            push_heap(large.begin(), large.end(), minComp);
        }
        else if (large.size() > small.size() + 1)
        {
            int smallest_large_val = large.front();
            pop_heap(large.begin(), large.end(), minComp);
            large.pop_back();
            small.push_back(smallest_large_val);
            push_heap(small.begin(), small.end(), maxComp);
        }
    }

    double findMedian()
    {
        cout << small.size() << large.size();
        if (small.size() > large.size())
            return small.front();
        else if (small.size() < large.size())
            return large.front();
        return (float(small.front() + large.front()) / 2);
    }

private:
    vector<int> small; // min heap
    vector<int> large; // max heap

    // declaring comparator
    // static bool minComp(int a, int b){ // this is needed so that the other classes can access (no this pointer)
    //     return a > b;
    // }

    // approach using std lib functions (lambda functions)
    function<bool(int, int)> minComp = [](int a, int b)
    { return a > b; };
    function<bool(int, int)> maxComp = [](int a, int b)
    { return a < b; };

    // apprach three, functors
    // struct comp {
    //     bool operator()(int a, int b) const {
    //         return a > b;
    //     }
    // };

    // comp minComp;
};
