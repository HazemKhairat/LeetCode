class Solution {
public:
    vector<int> findOrder(int n, vector<vector<int>>& p) {
        vector<vector<int>> graph(n);
        vector<int> indegree(n);
        vector<int> ans;

        for (auto edge : p) {
            graph[edge[0]].push_back(edge[1]);
            indegree[edge[1]]++;
        }
        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }

        while (!q.empty()) {
            int node = q.front();
            q.pop();
            ans.push_back(node);
            for (auto nighbour : graph[node]) {
                indegree[nighbour]--;
                if (indegree[nighbour] == 0) {
                    q.push(nighbour);
                }
            }
        }

        reverse(ans.begin(), ans.end());
        if (ans.size() == n) {
            return ans;
        }
        return {};
    }
};