#include <cstddef>

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

bool hasPathSum(TreeNode *root, int targetSum)
{
    if (root == NULL)
        return false;

    targetSum -= root->val; // automatically only saves this time

    if (root->right == nullptr && root->left == nullptr)
    {
        return targetSum == 0;
    }

    return hasPathSum(root->left, targetSum) || hasPathSum(root->right, targetSum);
}
