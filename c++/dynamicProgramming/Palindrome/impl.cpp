#include <string>

using namespace std;

/*
    The following is an O(n^2) implementation of determining the longest palindromic substring. It isn't tradiitonal dynamic programming
    but is nonetheless a good example of reducing repeated work.
    The brute force implementation goes through each substring (which is O(n^2)) and then iteraters through it with two pointers
    hence has a O(n^3) time complexity. This decreases the extra work.
*/

class Solution
{
public:
    string longestPalindrome(string s)
    {
        string res = "";

        // odd
        for (int i = 0; i < s.size(); i++)
        {
            string curr_res = "";
            curr_res += s[i];
            int l = i - 1, r = i + 1;
            while (l >= 0 && r < s.size() && s[l] == s[r])
            {
                curr_res = s[l--] + curr_res + s[r++];
                cout << curr_res << " " << l << " " << r << endl;
            }
            res = curr_res.size() > res.size() ? curr_res : res; // can assign to self
        }

        // even
        for (int i = 0; i < s.size(); i++)
        {
            string curr_res = "";
            int l = i, r = i + 1;
            while (l >= 0 && r < s.size() && s[l] == s[r])
            {
                curr_res = s[l--] + curr_res + s[r++];
            }
            res = curr_res.size() > res.size() ? curr_res : res;
        }

        return res;
    }
};
