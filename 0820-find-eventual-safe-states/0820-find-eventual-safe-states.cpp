class Solution {
public:
    vector<bool> visited, terminal, safe;
    vector<int> res;
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        res = vector<int>();
        visited = vector<bool>(n, false);
        terminal = vector<bool>(n, false);
        safe = vector<bool>(n, false);

        for (int i = 0; i < n; i++) {
            dfs(graph, i);
        }

        sort(res.begin(), res.end());
        return res;
    }

    void dfs(vector<vector<int>>& graph, int node) {
        if (visited[node]) {
            return;
        }
        visited[node] = true;
        if (graph[node].empty()) {
            terminal[node] = true;
            res.push_back(node);
            return;
        }
        bool isSafe = true;
        for (auto edge : graph[node]) {
            dfs(graph, edge);
            if (!terminal[edge] && !safe[edge]) {
                isSafe = false;
            }
        }
        if (isSafe) {
            safe[node] = true;
            res.push_back(node);
        }
    }
};