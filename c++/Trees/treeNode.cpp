class TreeNode {
    public:
        int val;
        TreeNode * left;
        TreeNode * right;

        TreeNode(int val)
        : val(val), left(nullptr), right(nullptr) {}
};


// Alternatively (and more commonly) with structs

struct TNode {
    int val;
    TNode * left;
    TNode * right;
    TNode() : val(0), left(nullptr), right(nullptr) {}
    TNode(int val) : val(val), left(nullptr), right(nullptr) {}
    TNode(int val, TNode * left, TNode * right) : val(0), left(nullptr), right(nullptr) {}
};



// searching for a node there

TreeNode *searchBST(TreeNode *root, int val)
{
    if (root == NULL) return NULL; // or !root

    if (root->val < val)
    {
        return searchBST(root->right, val);
    }
    else if (root->val > val)
    {
        return searchBST(root->left, val);
    }
    else
    {
        return root;
    }
    return NULL;
}


// Inserting into the BST like this:

TreeNode *insertIntoBST(TreeNode *root, int val)
{
    if (root == NULL)
    {
        TreeNode *new_node = new TreeNode(val);
        return new_node;
    }

    if (root->val < val)
    {
        root->right = insertIntoBST(root->right, val);
    }

    else
    {
        root->left = insertIntoBST(root->left, val);
    }
    return root;
}


// Deleting from the BST

TreeNode *deleteNode(TreeNode *root, int key)
{
    if (root == nullptr)
        return nullptr;

    else if (root->val < key)
    {
        root->right = deleteNode(root->right, key);
    }
    else if (root->val > key)
    {
        root->left = deleteNode(root->left, key);
    }
    else
    {
        if (root->left == nullptr)
        {
            return root->right; // sets it to nullptr if no leaf nodes
        }
        else if (root->right == nullptr)
        {
            return root->left; // These return statements don't modify the oritinal val, thus we need to set them
        }
        else
        {
            int min_val = find_min(root->right);
            root->right = deleteNode(root->right, min_val);
            root->val = min_val;
        }
    }
    return root;
}

// finding the min value

int find_min(TreeNode *root)
{
    while (root != nullptr && root->left != nullptr)
    {
        root = root->left;
    }
    return root->val;
}