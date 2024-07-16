#include <vector>

using namespace std;

/**
 * The following is an implementation of segmentation trees.
 * These are useful for range based queries with updates.
 * Worst case range-based queries are O(n). This method allows O(1) updates.
 * The prefix-suffix implmentation allows for an O(1) determination of ranges, but requires O(n) to create and doesn't allow updates (they would also be O(n)).
 * This method of the segment trees allows for an O(n) time for creating but allows updates and range based queries in O(log n) time.
 * Why O(log n) for querying? Refer to https://vscode.dev/github/AdvaySingh1/LeetCode_DSA/blob/main/c%2B%2B/Trees/SegmentationTrees/impl.cpp#L88 (line 88).
 * Here since each node has a value rather than just the sum, the max number of nodes accessed at any height in the tree is 4, hence, O(log n).
 * This can also be implemented with arrays. However, the last two  levels are not always complete like heaps and therefore this implementation is preferred.
 */

class Node
{
public:
    int sum;
    int L;
    int R;
    Node *left = nullptr;
    Node *right = nullptr;

    Node(int sum, int L, int R)
        : sum(sum), L(L), R(R) {}
};

class SegmentTree
{
public:
    SegmentTree(vector<int> &nums)
    {
        root = _build(nums, 0, nums.size() - 1);
    }

    void update(int index, int val)
    {
        _update(root, index, val);
    }

    int query(int L, int R)
    {
        return _query(root, L, R);
    }

private:
    Node *root;

    // private helper functions

    Node *_build(vector<int> &v, int L, int R)
    {
        if (L == R)
        {
            return new Node(v[L], L, R);
        }
        int m = (R + L) / 2;
        Node *root = new Node(0, L, R);
        root->left = _build(v, L, m);
        root->right = _build(v, m + 1, R);

        root->sum = root->left->sum + root->right->sum;

        return root;
    }

    void _update(Node *root, int index, int val)
    {
        if (root->L == root->R)
        {
            root->sum = val;
            return;
        }
        int m = (root->L + root->R) / 2;
        if (m >= index)
        {
            _update(root->left, index, val);
        }
        else
        {
            _update(root->right, index, val);
        }
        root->sum = root->left->sum + root->right->sum;
    }

    int _query(Node *root, int L, int R)
    {
        if (root->L == root->R || (root->L == L && root->R == R))
        {
            return root->sum;
        }

        int m = (root->L + root->R) / 2;

        if (L > m)
        {
            return _query(root->right, L, R);
        }
        else if (R <= m)
        {
            return _query(root->left, L, R);
        }
        else
        {
            return _query(root->left, L, m) + _query(root->right, m + 1, R);
        }
    }
};
