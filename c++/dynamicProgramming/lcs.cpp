#include <string>
#include <vector>

using namespace std;
class Solution
{
public:
    int longestCommonSubsequence(string text1, string text2)
    {
        this->text1 = text1;
        this->text2 = text2;

        /* optimized tabular two solution */
        if (text2.length() < text1.length())
        {
            this->text2 = text2;
            this->text1 = text1;
        }
        else
        {
            this->text2 = text1;
            this->text1 = text2;
        }
        int col = this->text2.length();
        int row = this->text1.length();
        cache = vector<vector<int>>(row + 1, vector<int>(col + 1, 0));

        // O(m) space and O(n * m) time tabular
        return tab2();

        // normal tabular
        return tab1();

        // memoization O(m * n) time and space.
        return memo(0, 0); // change defaults to -1 to implement

        // brute force solution O(m + n) space (height of tree) and O(2^(m + n)) time.
        return bruteForce(0, 0);
    }

private:
    string text1; // the longer one (rows)
    string text2; // shorter (cols) for memory in tabular2
    vector<vector<int>> cache;

    int tab2()
    {
        vector<int> cache(text2.size() + 1, 0);

        for (int r = 1; r < text1.length() + 1; r++)
        {
            vector<int> newCache(text2.size() + 1, 0);
            for (int c = 1; c < text2.length() + 1; c++)
            {
                if (text2[c - 1] == text1[r - 1])
                {
                    newCache[c] = 1 + cache[c - 1];
                }
                else
                {
                    newCache[c] = max(newCache[c - 1], cache[c]);
                }
            }
            cache = newCache;
        }
        return cache[text2.size()];
    }

    int tab1()
    {
        for (int r = 1; r < text1.length() + 1; r++)
        {
            for (int c = 1; c < text2.length() + 1; c++)
            {
                if (text2[c - 1] == text1[r - 1])
                {
                    cache[r][c] = 1 + cache[r - 1][c - 1];
                }
                else
                {
                    cache[r][c] = max(cache[r - 1][c], cache[r][c - 1]);
                }
            }
        }
        return cache[text1.length()][text2.length()];
    }

    int memo(int i1, int i2)
    {
        if (i1 >= text1.length() || i2 >= text2.length())
            return 0;

        if (cache[i1][i2] != -1)
            return cache[i1][i2];

        if (text1[i1] == text2[i2])
        {
            cache[i1][i2] = 1 + bruteForce(i1 + 1, i2 + 1);
        }
        else
        {
            cache[i1][i2] = max(bruteForce(i1 + 1, i2), bruteForce(i1, i2 + 1));
        }
        return cache[i1][i2];
    }

    int bruteForce(int i1, int i2)
    {
        if (i1 >= text1.length() || i2 >= text2.length())
            return 0;
        if (text1[i1] == text2[i2])
            return 1 + bruteForce(i1 + 1, i2 + 1);
        return max(bruteForce(i1 + 1, i2), bruteForce(i1, i2 + 1));
    }
};
