#include <map>
using namespace std;

class Solution
{
public:
    int climbStairs(int n)
    {

        /* bottom up apprach O(n) time and O(1) space */
        if (n <= 2)
        {
            return n;
        }
        int a[2] = {1, 2};

        for (int i = 3; i < n + 1; i++)
        {
            int tmp(a[1]);
            a[1] = a[0] + a[1];
            a[0] = tmp;
        }
        return a[1];

        /* Memorizatoin approach. O(n) time and space */
        // if (n <= 2){
        //     return n;
        // }
        // if (arr.find(n) != arr.end()){
        //     return arr[n];
        // }
        // else {
        //     arr[n] = climbStairs(n - 1) + climbStairs(n - 2);
        // }
        // return arr[n];

        /* Brute force approach. O(2^n) time and space O(n) */
        // if (n <= 2){
        //     return n;
        // }

        // return climbStairs(n - 1) + climbStairs(n - 2);
    }

private:
    map<int, int> arr;
};
