class Solution {
public:
    int minReorder(int n, vector<vector<int>>& connections) {
        vector<vector<pair<int, int>>> graph(n);
        for (auto con : connections) {
            int u = con[0], v = con[1];
            graph[u].push_back({v, 1});
            graph[v].push_back({u, 0});
        }

        int res = 0;
        queue<pair<int, int>> q;
        vector<int> visited(n, false);
        q.push({0, 0});
        while (!q.empty()) {
            int node = q.front().first;
            q.pop();
            visited[node] = true;
            for (auto nighbour : graph[node]) {
                // cout << nighbour.first << endl;
                if (!visited[nighbour.first]) {
                    if (nighbour.second == 1) {
                        res++;
                    }
                    q.push(nighbour);
                }
            }
        }

        return res;
    }
};