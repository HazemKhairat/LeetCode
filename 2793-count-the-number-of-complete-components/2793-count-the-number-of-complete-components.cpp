class Solution {
public:
    vector<vector<int>> graph;
    vector<int> visited;
    int countCompleteComponents(int n, vector<vector<int>>& edges) {
        // vector<vector<int>> graph(n);
        graph.resize(n);
        visited.resize(n + 5);

        for (auto edge : edges) {
            int u = edge[0], v = edge[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        int res = 0;
        for (int i = 0; i < n; i++) {

            if (!visited[i]) {
                int nodes = 1, edges = 0;
                dfs(i, nodes, edges);
                if (((nodes * (nodes - 1)) / 2) == (edges / 2)) {
                    res++;
                }
            }
        }

        return res;
    }

    void dfs(int node, int& nodesNum, int& edgesNum) {
        visited[node] = true;
        for (auto nighbour : graph[node]) {
            edgesNum++;
            if (!visited[nighbour]) {
                nodesNum++;
                dfs(nighbour, nodesNum, edgesNum);
            }
        }
    }
};