class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> graph;
    vector<bool> visited;
    vector<int> lowLink;
    vector<int> id;
    int time = 0;

    vector<vector<int>> criticalConnections(int n,
                                            vector<vector<int>>& connections) {
        graph.resize(n);
        visited.resize(n);
        lowLink.resize(n);
        id.resize(n);

        for (int i = 0; i < connections.size(); i++) {
            int u = connections[i][0], v = connections[i][1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, i);
            }
        }
        return res;
    }

    void dfs(int node, int parent) {
        id[node] = lowLink[node] = time++;
        visited[node] = true;

        for (auto nighbour : graph[node]) {

            if (parent == nighbour)
                continue;
            if (!visited[nighbour]) {
                dfs(nighbour, node);
                lowLink[node] = min(lowLink[node], lowLink[nighbour]);
                if (id[node] < lowLink[nighbour]) {
                    res.push_back({node, nighbour});
                }
            } else {
                lowLink[node] = min(lowLink[node], id[nighbour]);
            }
        }
    }
};