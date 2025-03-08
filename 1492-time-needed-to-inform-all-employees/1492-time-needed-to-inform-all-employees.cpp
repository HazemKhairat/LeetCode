class Solution {
public:
    int numOfMinutes(int n, int headID, vector<int>& manager,
                     vector<int>& informTime) {
        // node, cost
        int headCost = 0;
        vector<vector<pair<int, int>>> graph(n);
        for (int i = 0; i < n; i++) {
            if (i == headID) {
                headCost = informTime[i];
                continue;
            }
            int u = i, v = manager[i], cost = informTime[i];
            graph[v].push_back({u, cost});
        }

        return headCost + dfs(headID, graph);
    }

    int dfs(int node, vector<vector<pair<int, int>>>& graph) {
        if (graph[node].empty()) {
            return 0;
        }

        int sum = 0;
        for (auto p : graph[node]) {
            int neighbour = p.first, cost = p.second;
            sum = max(sum, cost + dfs(neighbour, graph));
        }

        return sum;
    }
};