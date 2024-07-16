#include <vector>
#include <stack>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    vector<int> preorderTraversal(TreeNode *root)
    {
        vector<int> res;
        stack<TreeNode *> nodes;
        TreeNode *curr = root;

        while (nodes.size() > 0 || curr != NULL)
        {
            if (curr != nullptr)
            {
                nodes.push(curr->right);
                res.push_back(curr->val);
                curr = curr->left;
            }
            else
            {
                curr = nodes.top();
                nodes.pop();
            }
        }

        return res;
    }
};