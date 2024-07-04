#include <iostream>
#include <vector> // use as queue
#include <queue>

using namespace std;

struct TreeNode {
    int val;
    TreeNode * left;
    TreeNode * right;

    TreeNode() 
        :val(0), left(nullptr), right(nullptr){}

    TreeNode(int val)
        : val(val), left(nullptr), right(nullptr) {}
    TreeNode(int val, TreeNode * left, TreeNode * right)
        : val(0), left(left), right(right) {}
};

void bfs(TreeNode * root){
    queue<TreeNode*> q;

    q.push(root);

    int level = 0;

    while(q.size() >= 0){

        cout << level;
        int length = q.size(); // need to declare before here
        for (int i = 0; i < length; i++){ // these are the nodes on that level (appended from the last iteration)

            TreeNode * curr = q.front(); q.pop();
            cout << curr->val << endl;

            if (curr->left) q.push(curr->left);
            if (curr->right) q.push(curr->right);
        
        }
        level++;
    }

}
;


