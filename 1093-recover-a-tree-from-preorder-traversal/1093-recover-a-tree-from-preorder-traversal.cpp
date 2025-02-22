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
    TreeNode* recoverFromPreorder(string traversal) {
        stack<TreeNode*> stk;
        for (int i = 0; i < traversal.size();) {
            int depth = 0;
            while (i < traversal.size() && !isdigit(traversal[i])) {
                depth++;
                i++;
            }
            string str = "";
            while (i < traversal.size() && isdigit(traversal[i])) {
                str.push_back(traversal[i]);
                i++;
            }
            int num = stoi(str);

            TreeNode* node = new TreeNode(num);

            while (stk.size() > depth) {
                stk.pop();
            }

            if (!stk.empty()) {
                if (stk.top()->left == NULL) {
                    stk.top()->left = node;
                } else {
                    stk.top()->right = node;
                }
            }

            stk.push(node);
        }

        while (stk.size() > 1) {
            stk.pop();
        }

        return stk.top();
    }
};