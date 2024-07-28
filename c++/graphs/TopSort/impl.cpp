#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

/**
 *  Time and space complexity.
        Initializing the adjacency list takes (O(V)) time since you're iterating over all vertices. (This is done within DFS for c++).
        Building the adjacency list from edges takes (O(E)) time since you're iterating over all edges.
        The DFS function, when called for each vertex, will visit each vertex and each edge exactly once, leading to (O(V + E)) time.
    Hence O(V + E).


    Space complexity:
        Adjacency List: Requires (O(V + E)) space.
        Visited and Path Sets: Each can grow up to (O(V)) space.
        Result List: Will store all vertices, so it requires (O(V)) space.
        Recursion Stack: In the worst case, the depth of the recursion stack can be (O(V)).
    Hence O(V + E).
 */

class Solution
{
public:
    vector<int> topologicalSort(int n, vector<vector<int>> &edges)
    {
        for (const auto &e : edges)
        {
            adj_l[e.front()].push_back(e.back());
        }
        for (int i = 0; i < n; i++)
        {
            if (!dfs(i))
            {
                return {};
            }
        }
        reverse(topSort.begin(), topSort.end());
        return topSort;
    }

private:
    bool dfs(const int src)
    {
        if (path.count(src))
            return false;
        if (visited.count(src))
            return true;
        visited.insert(src);
        path.insert(src);

        for (int n : adj_l[src])
        { // this will create numbers that don't exist
            if (!dfs(n))
            {
                return false;
            }
        }
        path.erase(src);
        topSort.push_back(src);
        return true;
    }

    unordered_map<int, vector<int>> adj_l;
    unordered_set<int> path, visited;
    vector<int> topSort;
};
