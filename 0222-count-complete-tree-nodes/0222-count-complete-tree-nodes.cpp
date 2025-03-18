/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
public:
    int countNodes(TreeNode* root) {
        if(root == nullptr) return 0;
        int res = 0;
        dfs(res, root);
        return res + 1;
    }

    void dfs(int& res, TreeNode* root) {
        if(!root){
            return;
        }
        else if (root->left && root->right) {
            res += 2;
        } else if (root->left || root->right) {
            res++;
        }
        dfs(res, root->left);
        dfs(res, root->right);
    }
};