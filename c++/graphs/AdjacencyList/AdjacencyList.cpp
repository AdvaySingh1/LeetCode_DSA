/**
 * Implement an adgency list for each of the nodes in the graph.
 * Refer to python for more details
 * Use a hashmap to store all of the nodes and a set for each of it's neighbors as the value.
 */

#include <map>
#include <set>
#include <queue>
#include <deque>

using namespace std;

class Graph
{
public:
    Graph() {}

    void addEdge(int src, int dst)
    {
        // c++ [] operater already adds the src
        graph[src].insert(dst);
    }

    bool removeEdge(int src, int dst)
    {
        if (graph.find(src) == graph.end() || graph[src].find(dst) == graph[src].end())
        {
            return false;
        }

        graph[src].erase(dst);
        return true;
    }

    bool hasPath(int src, int dst)
    {
        set<int> visited;
        // return hasPathDfs(src, dst, visited);
        return hasPathBfs(src, dst);
    }

private:
    map<int, set<int>> graph;

    bool hasPathDfs(int s, int d, set<int> &visited)
    {
        if (s == d)
        {
            return true;
        }
        else if (visited.find(s) != visited.end())
        {
            return false;
        }
        visited.insert(s);

        for (int elt : graph[s])
        {
            if (hasPathDfs(elt, d, visited))
            {
                return true;
            }
        }
        visited.erase(s);

        return false;
    }

    bool hasPathBfs(int s, int d)
    {
        deque<int> q = {s};
        set<int> visited;

        while (q.size() > 0)
        {
            int l = q.size();
            for (int i = 0; i < l; i++)
            {
                int n = q.front();
                q.pop_front();

                if (n == d)
                {
                    return true;
                }
                visited.insert(n);

                for (const int &elt : graph[n])
                {
                    if (visited.find(elt) == visited.end())
                    {
                        q.push_back(elt);
                    }
                }
            }
        }
        return false;
    }
};
