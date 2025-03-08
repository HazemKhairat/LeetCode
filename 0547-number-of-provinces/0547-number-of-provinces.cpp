class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<vector<int>> graph(n + 1);
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (i == j)
                    continue;
                if (isConnected[i - 1][j - 1]) {
                    graph[i].push_back(j);
                }
            }
        }

        int res = 0;
        vector<bool> visited(n + 1, false);
        for (int i = 1; i <= n; i++) {
            if (!visited[i]) {
                res++;
                dfs(graph, i, visited);
            }
        }

        return res;
    }

    void dfs(vector<vector<int>>& graph, int node, vector<bool>& visited) {
        visited[node] = true;
        for (auto nighbour : graph[node]) {
            if (!visited[nighbour]) {
                dfs(graph, nighbour, visited);
            }
        }
    }
};