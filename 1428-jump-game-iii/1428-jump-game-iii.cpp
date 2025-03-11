class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        int n = arr.size();
        vector<vector<int>> graph(n);
        for (int i = 0; i < n; i++) {
            int prev = i - arr[i], next = i + arr[i];
            if (prev >= 0) {
                graph[i].push_back(prev);
            }
            if (next < n) {
                graph[i].push_back(next);
            }
        }

        vector<bool> vis(n);
        vis[start] = true;
        return dfs(graph, start, vis, arr);

        // for(int i = 0; i < n; i++){
        //     cout << i << " => : ";
        //     for(auto item : graph[i]){
        //         cout << item << " ";
        //     }
        //     cout <<endl;
        // }
    }

    bool dfs(vector<vector<int>>& graph, int node, vector<bool>& vis,
             vector<int>& arr) {
        if (arr[node] == 0) {
            return true;
        }

        for (auto nighbour : graph[node]) {
            if (vis[nighbour])
                continue;
            vis[nighbour] = true;
            if (dfs(graph, nighbour, vis, arr)) {
                return true;
            }
        }

        return false;
    }
};