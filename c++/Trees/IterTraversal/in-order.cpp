#include <vector>
#include <stack>
#include <queue>

using namespace std;

/**
 * The following impl is also the same time and space complexity as the recursive iteration (O(n) space and O(n) time (prove using divide and conquer strong induction)).
 * Difference from the normal recursive implementation: we have our own cute lil stack.
 *
 * What to prove: T(n) = T(k) + T(n-k-1) + O(1) = O(n) (omega in this case).
 */

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class BSTIterator
{
public:
    BSTIterator(TreeNode *root)
    {
        TreeNode *curr = root;

        while (curr != NULL || stack.size() > 0)
        {
            if (curr != NULL)
            {
                stack.push(curr);
                curr = curr->left;
            }
            else
            {
                curr = stack.top();
                stack.pop();
                res.push(curr->val);
                curr = curr->right;
            }
        }
    }

    int next()
    {
        // int val = res.top(); res.erase(res.begin());
        int val = res.front();
        res.pop(); // in-order traversal using queues in c++ for O(1) removal rather than O(n)
        return val;
    }

    bool hasNext()
    {
        return (res.size() > 0);
    }

private:
    // vector<int> res;
    queue<int> res;
    stack<TreeNode *> stack;
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */