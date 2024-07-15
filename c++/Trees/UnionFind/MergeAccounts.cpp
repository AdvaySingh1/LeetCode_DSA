#include <unordered_map>>
#include <vector>
#include <string>

using namespace std;

class UnionFind
{
public:
    UnionFind(int n)
    {
        par = new int[n];
        rank = new int[n];

        for (int i = 0; i < n; i++)
        {
            par[i] = i;
        }
    }

    int find(int x)
    {
        if (par[x] != x)
        {
            par[x] = find(par[x]); // makes it the first node
        }
        return par[x];
    }

    const bool _union(int x, int y)
    {
        int xp = find(x), yp = find(y);

        if (xp == yp)
            return false;

        if (rank[xp] > rank[yp])
        {
            par[yp] = xp;
        }
        else if (rank[xp] < rank[yp])
        {
            par[xp] = yp;
        }
        else
        {
            par[yp] = xp;
            rank[xp]++;
        }
        return true;
    }

private:
    int *par;
    int *rank;
};

class Solution
{
public:
    vector<vector<string>> accountsMerge(vector<vector<string>> &accounts)
    {
        unordered_map<string, int> emailToIndex; // implementing unordered to use hasing for O(1)

        UnionFind uf = UnionFind(accounts.size());

        for (int i = 0; i < accounts.size(); i++)
        {
            for (int j = 1; j < accounts[i].size(); j++)
            {
                string email = accounts[i][j];
                if (emailToIndex.count(email) > 0)
                {
                    uf._union(i, emailToIndex[email]);
                }
                else
                {
                    emailToIndex.insert({email, i});
                }
            }
        }

        vector<vector<string>> res;
        unordered_map<int, vector<string>> emailGroup;

        for (pair<string, int> elt : emailToIndex)
        {
            int parent = uf.find(elt.second);
            emailGroup[parent].push_back(elt.first);
        }

        for (pair<int, vector<string>> elt : emailGroup)
        {
            vector<string> list;
            list.push_back(accounts[elt.first][0]);
            sort(elt.second.begin(), elt.second.end()); // O(n log n) for quick sort (with right pivot) or merge sort
            list.insert(list.end(), elt.second.begin(), elt.second.end());
            res.push_back(list);
        }

        return res;
    }
};