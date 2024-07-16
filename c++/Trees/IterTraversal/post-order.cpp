#include <vector>
#include <stack>

// two stacks

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
    vector<int> postorderTraversal(TreeNode *root)
    {
        vector<int> res;
        stack<TreeNode *> nodes;
        stack<bool> visited;
        nodes.push(root);
        visited.push(false);

        while (nodes.size() > 0)
        {
            TreeNode *curr = nodes.top();
            nodes.pop(); // front for queue
            bool v = visited.top();
            visited.pop();
            if (curr != NULL)
            {
                if (v)
                {
                    res.push_back(curr->val);
                }
                else
                {
                    nodes.push(curr);
                    visited.push(true);
                    nodes.push(curr->right);
                    visited.push(false);
                    nodes.push(curr->left);
                    visited.push(false);
                }
            }
        }

        return res;

        /* The following is the recursive implementation */
        //     _helper(root, res);
        //     return res;
        // }

        // void _helper(TreeNode * root, vector<int>& res) {
        //     if (root != nullptr){
        //         _helper(root->left, res);
        //         _helper(root->right, res);
        //         res.push_back(root->val);
        //     }
    }
};