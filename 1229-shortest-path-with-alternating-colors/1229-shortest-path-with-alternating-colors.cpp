class Solution {
public:
    vector<int> shortestAlternatingPaths(int n, vector<vector<int>>& redEdges,
                                         vector<vector<int>>& blueEdges) {
        vector<vector<pair<int, int>>> graph(n);
        vector<int> ans(n, -1);
        vector<vector<bool>> visited(n, vector<bool>(2, false));
        for (auto edge : redEdges) {
            int u = edge[0], v = edge[1];
            graph[u].push_back({v, 1});
        }
        for (auto edge : blueEdges) {
            int u = edge[0], v = edge[1];
            graph[u].push_back({v, 0});
        }

        visited[0][0] = visited[0][1] = true;
        ans[0] = 0;
        queue<vector<int>> q;
        q.push({0, -1, 0}); // node, prev, cost;
        while (!q.empty()) {
            int node = q.front()[0], prev = q.front()[1], cost = q.front()[2];
            // cout << node << endl;
            q.pop();

            for (auto& nighbour : graph[node]) {
                int nextNode = nighbour.first, color = nighbour.second;
                if(!visited[nextNode][color] && color != prev){
                    visited[nextNode][color] = true;
                    q.push({nextNode, color, cost + 1});

                    if(ans[nextNode] == -1){
                        ans[nextNode] = cost + 1;
                    }
                }
                
            }
        }

        return ans;
    }
};