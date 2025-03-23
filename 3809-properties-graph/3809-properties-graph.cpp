class Solution {
public:
    vector<vector<int>> graph;
    vector<bool> visited;
    int numberOfComponents(vector<vector<int>>& prop, int k) {
        int n = prop.size();
        visited.resize(n + 5, false);
        graph.resize(n);
        for (int i = 0; i < prop.size(); i++) {
            unordered_set<int> st1(prop[i].begin(), prop[i].end());
            for (int j = i + 1; j < prop.size(); j++) {
                unordered_set<int> st2(prop[j].begin(), prop[j].end());
                if (intersect(st1, st2) >= k) {
                    graph[i].push_back(j);
                    graph[j].push_back(i);
                }
            }
        }

        int res = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                res++;
                dfs(i);
            }
        }
        return res;
    }

    void dfs(int node) {
        visited[node] = true;
        for (auto nighbour : graph[node]) {
            if (!visited[nighbour]) {
                dfs(nighbour);
            }
        }
    }

    int intersect(unordered_set<int>& a, unordered_set<int>& b) {
        int res = 0;
        for (int num : a) {
            if (b.count(num)) {
                res++;
            }
        }
        return res;
    }
};