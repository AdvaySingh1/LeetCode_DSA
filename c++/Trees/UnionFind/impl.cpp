
#include <map>
using namespace std;
/**
 * Union find algorithm with path compression in the find algorithms
 * What happens to the rank? Time complexity if O(ElogV) but reduces to O(1)?
 * More on this here: https://www.geeksforgeeks.org/union-by-rank-and-path-compression-in-union-find-algorithm/
 * Useful when you want to see connected aspects of a graph.
 */
class UnionFind
{

private:
    map<int, int> par;
    map<int, int> rank;
    int num_comp;

public:
    UnionFind(int n)
        : num_comp(n)
    {
        for (int i = 0; i < n; i++)
        {
            par[i] = i;
            rank[i] = 0;
        }
    }

    int find(int x)
    {
        if (par[x] != x)
        {
            par[x] = find(par[x]);
        }
        return par[x];
    }

    bool isSameComponent(int x, int y)
    {
        return (find(x) == find(y));
    }

    // Union is a reserved keyword in C++, so we use _union instead
    bool _union(int x, int y)
    {
        int xp = find(x), yp = find(y);
        if (xp == yp)
            return false;

        if (rank[xp] > rank[yp])
            par[yp] = xp;

        else if (rank[yp] > rank[xp])
            par[xp] = yp;

        else
        {
            par[yp] = xp;
            rank[xp] += 1;
        }
        num_comp--;
        return true;
    }

    int getNumComponents()
    {
        return num_comp;
    }
};
