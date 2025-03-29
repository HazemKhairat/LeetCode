class Solution {
public:
    vector<int> vis, colors;
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        colors.resize(n);
        vis.resize(n + 5);
        bool res = false;
        for (int i = 0; i < n; i++) {
            if (!vis[i] && !dfs(graph, 0, i)) {
                return false;
            }
        }
        return true;
    }

    bool dfs(vector<vector<int>>& graph, int c, int node) {
        vis[node] = true;
        colors[node] = c;
        for (auto nighbour : graph[node]) {
            if (!vis[nighbour]) {
                if (!dfs(graph, !c, nighbour)) {
                    return false;
                }
            } else {
                if (colors[nighbour] == colors[node]) {
                    return false;
                }
            }
        }
        return true;
    }
};