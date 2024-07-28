#include <algorithm>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

/**
 * Prims algorithm is used to find the minimum spanning tree. The time complexity of this is O(E * log(v)) and the space is O(E).
 */

class Solution
{
public:
    int minimumSpanningTree(vector<vector<int>> &edges, int n)
    {

        // create the adjcency list
        unordered_map<int, vector<pair<int, int>>> adj_l;

        for (const auto &edge : edges)
        {
            adj_l[edge[0]].push_back({edge[1], edge[2]});
            adj_l[edge[1]].push_back({edge[0], edge[2]});
        }

        unordered_set<int> visited;
        vector<pair<int, int>> heap;
        heap.push_back({0, 0});
        int sum = 0;

        while (visited.size() < n && heap.size() > 0)
        {
            int w = heap.front().first;
            int src = heap.front().second;

            pop_heap(heap.begin(), heap.end());
            heap.pop_back();

            if (visited.count(src) == 0)
            {
                sum -= w;
                visited.insert(src);

                for (const auto &c : adj_l[src])
                {
                    int dst = c.first;
                    int w2 = c.second;
                    if (visited.count(dst) == 0)
                    {
                        heap.push_back({-w2, dst});
                        push_heap(heap.begin(), heap.end());
                    }
                }
            }
        }

        return (visited.size() == n) ? sum : -1;
    }
};
