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
        if (!root) {
            return false;
        }
        int l = 1, r = 1;
        TreeNode *left = root, *right = root;
        while (left = left->left)
            l++;
        while (right = right->right)
            r++;
        if (l == r)
            return (1 << l) - 1;
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
};