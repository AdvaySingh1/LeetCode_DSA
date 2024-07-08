#include <vector>
#include <string>
#include <unordered_set>
using namespace std;

/**
 * The following is a bfs implementation for the shortest path.
 * The space complexity is O(N * M) because the queue and the visited can have all of the nodes in the matrix
 * The time complexity is )(N * M) since we are only going thorugh each of the items one time.
 */

class Solution
{
public:
    int shortestPath(vector<vector<int>> &grid)
    {
        vector<pair<int, int>> queue;
        unordered_set<string> visited;

        queue.push_back({0, 0});

        int pathCount = 0;

        while (queue.size() > 0)
        {
            int l = queue.size();
            for (int i = 0; i < l; i++)
            {
                int r = queue[0].first, c = queue[0].second;

                if (r == grid.size() - 1 && c == grid[0].size() - 1)
                {
                    return pathCount;
                }

                // vector<vector<int>> neighbors = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}}
                if (r < grid.size() && c < grid[0].size() && r >= 0 && c >= 0 && grid[r][c] == 0 &&
                    visited.find(to_string(r) + to_string(c)) == visited.end())
                {
                    queue.push_back({r + 1, c});
                    queue.push_back({r, c + 1});
                }

                visited.insert(to_string(r) + to_string(c));
                queue.erase(queue.begin());
            }
            pathCount++;
        }
        return -1;
    }
};
