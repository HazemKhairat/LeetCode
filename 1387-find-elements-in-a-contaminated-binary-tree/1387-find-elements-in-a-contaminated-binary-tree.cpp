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
class FindElements {
public:
    TreeNode* globalRoot;
    FindElements(TreeNode* root) {
        globalRoot = root;
        globalRoot->val = 0;
        recover(globalRoot);
    }

    void recover(TreeNode* root) {
        // cout << root->val << endl;
        if (root->left) {
            root->left->val = root->val * 2 + 1;
            recover(root->left);
        }
        if (root->right) {
            root->right->val = 2 * root->val + 2;
            recover(root->right);
        }
    }

    bool findElement(TreeNode* root, int target) {
        if (root == nullptr) {
            return false;
        }
        if (root->val == target) {
            return true;
        }
        return findElement(root->left, target) ||
               findElement(root->right, target);
    }
    bool find(int target) { return findElement(globalRoot, target); }
};

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements* obj = new FindElements(root);
 * bool param_1 = obj->find(target);
 */