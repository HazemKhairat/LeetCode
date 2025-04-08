class Solution {
public:
    vector<vector<int>> graph;
    vector<int> color;

    bool canFinish(int n, vector<vector<int>>& p) {
        /*
            - graph coloring alogrithm
            0 -> not proccessed
            1 -> proccessing
            2 -> proccessed
        */
        graph = vector<vector<int>>(n);
        color = vector<int>(n + 2);
        for (vector<int>& item : p) {
            graph[item[0]].push_back(item[1]);
        }

        for (int i = 0; i < n; i++) {
            if(color[i] == 0 && !dfs(i)){
                return false;
            }
        }
        return true;
    }

    bool dfs(int node) {
        if(color[node] == 1) // it is in proccess 
            return false;
        if(color[node] == 2){
            return true;
        }
        color[node] = 1;
        for (auto nighbour : graph[node]) {
            if(!dfs(nighbour)){
                return false;
            }
        }
        color[node] = 2;
        return true;
    }
};