#include <vector>

using namespace std;
// Definition for a binary tree node.
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
    bool isValidBST(TreeNode *root)
    {
        // recursive approach
        // return _isValidBST(-1001, root, 1001);

        // in order terversal apprach
        vector<TreeNode *> stack;
        TreeNode *curr = root;
        int min_val = INT_MIN;
        while (stack.size() > 0 || curr != nullptr)
        {
            while (curr != nullptr)
            {
                stack.push_back(curr);
                curr = curr->left;
            }
            if (curr == nullptr)
            {
                curr = stack.back();
                stack.pop_back();
                if (curr->val <= min_val)
                    return false;
                min_val = curr->val;
                curr = curr->right;
            }
        }
        return true;
    }

private:
    bool _isValidBST(int left, TreeNode *curr, int right)
    {
        if (curr == nullptr)
        {
            return true;
        }
        else if (left < curr->val && curr->val < right)
        {
            return (_isValidBST(left, curr->left, curr->val) &&
                    _isValidBST(curr->val, curr->right, right));
        }
        return false;
    }
};
