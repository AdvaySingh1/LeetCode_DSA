#include <vector>
using namespace std;

class Solution
{
public:
    int maximumProfit(vector<int> &profit, vector<int> &weight, int capacity)
    {
        this->profit = profit;
        this->weight = weight;

        // O(m * n) time and O(m) space dynamic programming
        return d2(capacity);

        // O(m * n) time and space dynamic prograsmming
        return d1(capacity);

        // O(m * n) time and space memorizaition
        for (int i = 0; i < profit.size(); i++)
        {
            cache.push_back({});
            for (int j = 0; j < capacity + 1; j++)
            {
                cache[i].push_back(-1); // sentinal value
            }
        }
        return memorization(0, capacity);

        // O(2^n) time and O(n) space (call stack)
        // return brute_force(0, capacity);
    }

private:
    vector<int> profit, weight;
    vector<vector<int>> cache;

    /* Brute force */
    int brute_force(int i, int cap)
    {
        if (i == profit.size())
            return 0;

        // exlude
        int exclude = brute_force(i + 1, cap), include = 0;
        // include
        int newCap = cap - weight[i];
        if (newCap >= 0)
        {
            include = profit[i] + brute_force(i + 1, newCap);
        }

        return max(include, exclude);
    } // brute_force

    /* Memorization */
    int memorization(int i, int cap)
    {
        if (i == profit.size())
            return 0;
        if (cache[i][cap] != -1)
            return cache[i][cap];

        // exlude
        int exclude = memorization(i + 1, cap), include = 0;

        // include
        int newCap = cap - weight[i];
        if (newCap >= 0)
        {
            include = profit[i] + memorization(i + 1, newCap);
        }
        cache[i][cap] = max(include, exclude);
        return cache[i][cap];
    } // memorization

    /* Dynamic Programming 1 */
    int d1(int capacity)
    {
        for (int i = 0; i < profit.size(); i++)
        {
            cache.push_back({});
            for (int j = 0; j < capacity + 1; j++)
            {
                cache[i].push_back(0);
            }
        }

        // init the first row
        for (int j = 0; j < capacity + 1; j++)
        {
            if (j - weight[0] >= 0)
            {
                cache[0][j] = profit[0];
            }
        }

        for (int i = 1; i < cache.size(); i++)
        {
            for (int j = 1; j < capacity + 1; j++)
            {
                // exclude
                int exclude = cache[i - 1][j], include = 0;

                // include
                if (j - weight[i] >= 0)
                {
                    include = profit[i] + cache[i - 1][j - weight[i]];
                }
                cache[i][j] = max(include, exclude);
            }
        }
        return cache[profit.size() - 1][capacity];
    } // d1

    /* Dynamic Programming Two */
    int d2(const int capacity)
    {
        vector<int> cache;
        for (int j = 0; j < capacity + 1; j++)
        {
            if (j - weight[0] >= 0)
            {
                cache.push_back(profit[0]);
            }
            else
            {
                cache.push_back(0);
            }
        }

        for (int i = 1; i < profit.size(); i++)
        {
            vector<int> newCache;
            for (int j = 0; j < capacity + 1; j++)
            {
                // exclude
                int exclude = cache[j], include = 0;
                // include
                if (j - weight[i] >= 0)
                {
                    include = profit[i] + cache[j - weight[i]];
                }
                newCache.push_back(max(include, exclude));
            }
            cache = newCache;
        }
        return cache[capacity];
    } // d2
};