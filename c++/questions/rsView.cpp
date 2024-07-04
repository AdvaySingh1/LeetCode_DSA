#include <vector>
#include <queue>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode()
        : val(0), left(nullptr), right(nullptr) {}

    TreeNode(int val)
        : val(val), left(nullptr), right(nullptr) {}
    TreeNode(int val, TreeNode *left, TreeNode *right)
        : val(0), left(left), right(right) {}
};

class Solution
{
public:
    vector<int> rightSideView(TreeNode *root)
    {
        queue<TreeNode *> q;
        vector<int> res;
        if (root == NULL)
            return res;
        q.push(root);

        while (q.size() > 0)
        {
            int r = q.size(), i = 0;
            for (; i < r; i++)
            {
                auto node = q.front();
                q.pop();
                if (i == r - 1)
                    res.push_back(node->val);
                if (node->left != nullptr)
                    q.push(node->left);
                if (node->right != nullptr)
                    q.push(node->right);
            }
        }

        return res;
    }
};