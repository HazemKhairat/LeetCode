class UnionFind {
public:
    vector<int> parent, rank;
    UnionFind(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    void Union(int n1, int n2) {
        int p1 = find(n1), p2 = find(n2);
        if (p1 == p2)
            return;
        if (rank[p1] < rank[p2]) {
            swap(p1, p2);
        }
        parent[p2] = p1;
        if (rank[p1] == rank[p2])
            rank[p1]++;
    }

    int find(int n) {
        if (parent[n] == n) {
            return n;
        }
        return parent[n] = find(parent[n]);
    }
};

class Solution {
public:
    vector<int> minimumCost(int n, vector<vector<int>>& edges,
                            vector<vector<int>>& query) {
        UnionFind uf(n);
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1];
            uf.Union(u, v);
        }

        vector<unsigned int> costs(n, -1);
        vector<int> res;
        for (auto& edge : edges) {
            int root = uf.find(edge[0]), w = edge[2];
            costs[root] &= w;
        }

        for (auto q : query) {
            int r1 = uf.find(q[0]), r2 = uf.find(q[1]);
            if (r1 != r2) {
                res.push_back(-1);
            } else {
                res.push_back(costs[r1]);
            }
        }

        return res;
    }
};
