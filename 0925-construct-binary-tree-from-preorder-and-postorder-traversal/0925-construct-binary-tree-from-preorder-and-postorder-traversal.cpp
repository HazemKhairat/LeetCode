class Solution {
public:
    TreeNode* constructFromPrePost(vector<int>& preorder,
                                   vector<int>& postorder) {
        int i = 0, j = 0;
        return dfs(i, j, preorder, postorder);
    }

    TreeNode* dfs(int& i, int& j, vector<int>& preorder,
                  vector<int>& postorder) {
        if (i >= preorder.size() || j >= postorder.size())
            return nullptr;
        TreeNode* node = new TreeNode(preorder[i]);
        if (node->val != postorder[j]) {
            i++;
            node->left = dfs(i, j, preorder, postorder);
        }
        if (node->val != postorder[j]) {
            i++;
            node->right = dfs(i, j, preorder, postorder);
        }
        j++;
        return node;
    }
};