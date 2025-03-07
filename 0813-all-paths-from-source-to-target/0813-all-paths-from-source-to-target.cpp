class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>> res;
        dfs(0, graph, res, {0});
        return res;
    }

    void dfs(int node, vector<vector<int>>& graph, vector<vector<int>>& res,
             vector<int> curr) {
        if (node == graph.size() - 1) {
            res.push_back(curr);
            return;
        }

        for (auto nighbour : graph[node]) {
            curr.push_back(nighbour);
            dfs(nighbour, graph, res, curr);
            curr.pop_back();
        }
    }
};