class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        vector<int> res;
        unordered_set<int> reachable;

        for (auto edge : edges) {
            int u = edge[0], v = edge[1];
            reachable.insert(v);
        }

        for (int i = 0; i < n; i++) {
            if (!reachable.count(i)) {
                res.push_back(i);
            }
        }

        return res;
    }
};