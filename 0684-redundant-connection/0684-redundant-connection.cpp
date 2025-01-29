class Solution {
public:
    vector<int> parent, rank;
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        parent = vector<int>(n + 1);
        rank = vector<int>(n + 1, 1);
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        for (auto edge : edges) {
            if (!_union(edge[0], edge[1])) {
                return {edge[0], edge[1]};
            }
        }

        return {};
    }

    int find(int node) {
        if (parent[node] == node) {
            return node;
        }
        return parent[node] = find(parent[node]);
    }
    bool _union(int node1, int node2) {
        int p1 = find(node1), p2 = find(node2);
        if (p1 == p2) {
            return false;
        }
        if (rank[p1] >= rank[p2]) {
            parent[p2] = p1;
            rank[p1] += rank[p2];
        } else {
            parent[p1] = p2;
            rank[p2] += rank[p1];
        }
        return true;
    }
};