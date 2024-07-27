#include <unordered_map>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

/**
 * The following is an implementation of Dijkstra's algorithms.
    The adj_m initially created is of the form:
        src1: [[dst1, w1], [dst2, w2]], ..., [dstn, wn]
        src2: [[dst1, w1], [dst2, w2]], ..., [dstn, wn]
    Normal adj_m are of the form
        src1: [dst1, dst2, ..., dstn]
        src2: [dst1, dst2, ..., dstn]

    If there is no root found, then we return -1.
    Dijkstra's algorithm is a greedy algorithm; we always choose the next best step. Due to this,
    we naturally end up choosing the most efficient path first. However, due to the nature of the question,
    we are unable to simply stop the dfs loop when the res is the same length as n because not all
    values within n are included in the edges. Some are disconnected regions and hence res will never be the same size.

    Time complexity discussion:
        The time complexity for creating adj_m:
            as we loop through each of the edges, with there being up to n - 1 edges for each vertex
            in the case of a fully connected graph, this operation is O(E) which is also the same thing as O(n^2).
            It's possible that none of the edges are connected, then this Ω(1).

        Time complexity for creating res:
            The DFS algorithm can have us visit each edge at most one time. Hence, a similar O(E) and Ω(1) logic applies.
            However, we do an additional step each of the time, the logarithmic addition or delition from the heap.
            Then we see a O(log ^ (E)). However, we can re-write this as O(log ^ (V^2)) = O(2 log ^ (V)).
            Therefore, the formal time complexity if O(log^(V)).

    The space complexity of O(E) or O(V^2) since we have to store each of the edges in the adj_m which is greater than O(V)
    which is needed for the res.
 */

class Solution
{
public:
    unordered_map<int, int> shortestPath(int n, vector<vector<int>> &edges, int src)
    {
        // firstly create a map of strings for the connected componenets
        unordered_map<int, vector<pair<int, int>>> adj_m;

        for (auto &elt : edges)
        {
            vector<int> vals;
            adj_m[elt.front()].push_back({elt[1], elt[2]});
        }

        for (auto k : adj_m)
        {
            cout << k.first << " size is " << k.second.size() << endl;
        }

        vector<pair<int, int>> queue;
        unordered_map<int, int> res;

        queue.push_back({0, src});
        push_heap(queue.begin(), queue.end());

        while (queue.size() > 0)
        {
            int s = queue.front().second;
            int w = queue.front().first;
            if (res.count(s) == 0)
            {
                res[s] = -w;
            }

            pop_heap(queue.begin(), queue.end());
            queue.pop_back();

            for (pair<int, int> &d : adj_m[s])
            {
                int des = d.first;
                int w2 = d.second;
                if (res.count(des) == 0)
                {
                    queue.push_back({w - w2, des});
                    push_heap(queue.begin(), queue.end());
                }
            }
        }

        // fill in the edges which can't be reached
        for (int i = 0; i < n; i++)
        {
            if (res.count(i) == 0)
            {
                res[i] = -1;
            }
        }

        return res;
    }

private:
    // function<bool(pair<int, int>, pair<int, int>) minComp = [](pair<int, int> a, pair<int, int> b) return a.first < b.first;
};
