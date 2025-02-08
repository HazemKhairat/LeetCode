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
    vector<int> v1, v2;
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        v1 = vector<int>();
        v2 = vector<int>();
        dfs(root1, v1);
        dfs(root2, v2);
        return v1 == v2;
    }

    void dfs(TreeNode* node, vector<int>& v) {
        if (node == nullptr) {
            return;
            ;
        }
        if (node->left == nullptr && node->right == nullptr) {
            v.push_back(node->val);
        }
        dfs(node->left, v);
        dfs(node->right, v);
    }
};