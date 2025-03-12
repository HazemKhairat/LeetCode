/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    map<int, vector<int>> graph;

    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        dfs(root);
        int n = graph.size();
        vector<bool> vis(n + 5);
        vis[target->val] = true;
        queue<int> q;
        q.push(target->val);
        while (!q.empty()) {
            int size = q.size();
            if (k == 0) {
                vector<int> res;
                while (!q.empty()) {
                    res.push_back(q.front());
                    q.pop();
                }
                return res;
            }
            for (int i = 0; i < size; i++) {
                int node = q.front();
                q.pop();
                for (auto nighbour : graph[node]) {
                    if (vis[nighbour])
                        continue;
                    q.push(nighbour);
                    vis[nighbour] = true;
                }
            }
            k--;
        }

        return {};
    }

    void dfs(TreeNode* root) {
        if (root == nullptr) {
            return;
        }
        if (root->left) {
            graph[root->val].push_back(root->left->val);
            graph[root->left->val].push_back(root->val);
            dfs(root->left);
        }
        if (root->right) {
            graph[root->val].push_back(root->right->val);
            graph[root->right->val].push_back(root->val);
            dfs(root->right);
        }
    }
};