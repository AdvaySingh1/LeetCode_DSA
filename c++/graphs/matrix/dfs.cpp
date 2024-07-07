#include <vector>
#include <string>
#include <unordered_set>
using namespace std;

/**
 * The following is a dfs implementation for the numbe of paths.
 * The space complexity is O(N * M) because that is the potentail size of the call stack.
 * The time complexity is O(4^(N * M) because we are going through each of the N * M elements
 *      with a backtracking approach where there are 4 options to choose from each time.
 *      picture a binary search tree here.
 */

class Solution
{
public:
    int countPaths(vector<vector<int>> &grid)
    {
        unordered_set<string> visited;

        return _helper(0, 0, visited, grid);
    }

private:
    int _helper(int r, int c, unordered_set<string> &visited, vector<vector<int>> &grid)
    {

        string cell = to_string(r) + "-" + to_string(c);
        if (visited.find(cell) != visited.end() || r >= grid.size() || c >= grid[0].size() || r < 0 || c < 0 || grid[r][c] == 1)
        {
            return 0;
        }

        else if (r == grid.size() - 1 && c == grid[0].size() - 1)
        {
            return 1;
        }

        visited.insert(cell);
        int count = 0;

        count += _helper(r + 1, c, visited, grid);
        count += _helper(r - 1, c, visited, grid);
        count += _helper(r, c + 1, visited, grid);
        count += _helper(r, c - 1, visited, grid);

        visited.erase(cell);

        return count;
    }
};