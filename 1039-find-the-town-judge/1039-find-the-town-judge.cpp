class Solution {
public:
    vector<vector<int>> graph;
    vector<bool> vis;
    int target = 0, count = 0, sum = 0;
    int findJudge(int n, vector<vector<int>>& trust) {
        graph = vector<vector<int>>(n + 1);
        vis = vector<bool>(n + 5);
        for (auto edge : trust) {
            graph[edge[0]].push_back(edge[1]);
        }
        // define the target node (empty node)
        // count num of empty node if there more than 1 -> return -1
        // count num of node connected to target if == n -> true else false

        for (int i = 1; i <= n; i++) {
            if (graph[i].empty()) {
                target = i;
                count++;
            }
        }
        cout << count << endl << target << endl;
        if (count > 1 || !target) {
            return -1;
        }

        for (int i = 1; i <= n; i++) {
            if (!vis[i]) {
                vis[i] = true;
                dfs(i);
            }
        }
        cout << sum << endl;
        return sum == n - 1 ? target : -1;
    }

    void dfs(int node) {
        for (auto nighbour : graph[node]) {
            if (nighbour == target) {
                sum++;
            }
            if (!vis[nighbour]) {

                vis[nighbour] = true;
                dfs(nighbour);
            }
        }
    }
};