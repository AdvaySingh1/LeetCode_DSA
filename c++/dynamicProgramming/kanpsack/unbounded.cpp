#include <vector>
using namespace std;

class Solution
{
public:
    int maximumProfit(vector<int> &profit, vector<int> &weight, int capacity)
    {
        this->profit = profit;
        this->weight = weight;

        // Tabular two apprach O(m) space, O(m * n) time.
        return tab2(capacity);

        // Memoization O(m) space apprach, O(m * n) time.
        return memo2(capacity);

        // Tabular one apprach O(m) space, O(m * n) time.
        return tab1(capacity);
    }

private:
    vector<int> profit;
    vector<int> weight;

    int tab2(int capacity)
    {
        int cache[capacity + 1];
        for (int i = 0; i < capacity + 1; i++)
        {
            cache[i] = 0;
            for (int j = 0; j < profit.size(); j++)
            {
                if (i - weight[j] >= 0)
                {
                    cache[i] = max(cache[i], profit[j] + cache[i - weight[j]]);
                }
            }
        }
        return cache[capacity];
    }

    unordered_map<int, int> cache; // has capacity
    int memo2(int cap)
    {
        if (cap == 0)
            return 0;
        if (cache.count(cap) > 0)
            return cache[cap];
        cache[cap] = 0;
        for (int i = 0; i < profit.size(); i++)
        {
            if (cap - weight[i] >= 0)
            {
                cache[cap] = max(cache[cap], profit[i] + memo2(cap - weight[i]));
            }
        }
        return cache[cap];
    }

    int tab1(int capacity)
    {
        int cache[capacity + 1];
        fill(cache, cache + capacity + 1, 0); // algo using iter

        for (int i = 0; i < profit.size(); i++)
        {
            int newCache[capacity + 1];
            for (int j = 0; j < capacity + 1; j++)
            {
                newCache[j] = cache[j];
                if (j - weight[i] >= 0)
                {
                    newCache[j] = max(newCache[j], profit[i] + newCache[j - weight[i]]);
                }
            }
            copy(newCache, newCache + capacity + 1, cache); // algo using iter
        }
        return cache[capacity];
    }
};
