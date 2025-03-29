class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> color(n); // 1 red, -1 blue

        queue<int> q;

        for (int i = 0; i < n; i++) {
            if (!color[i]) {
                q.push(i);
                color[i] = 1;
                while (!q.empty()) {
                    int size = q.size();
                    for (int i = 0; i < size; i++) {
                        int node = q.front();
                        q.pop();

                        for (auto nighbour : graph[node]) {
                            if (color[nighbour] == 0) {
                                q.push(nighbour);
                                color[nighbour] = color[node] * -1;
                            } else {
                                if (color[nighbour] == color[node]) {
                                    return false;
                                }
                            }
                        }
                    }
                }
            }
        }

        return true;
    }
};