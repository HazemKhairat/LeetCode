class Solution {
public:
    vector<int> parent, rank;
    int numberOfComponents(vector<vector<int>>& prop, int k) {
        int n = prop.size();

        parent.resize(n);
        rank.resize(n, 1);

        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < prop.size(); i++) {
            unordered_set<int> st1(prop[i].begin(), prop[i].end());

            for (int j = i + 1; j < prop.size(); j++) {
                unordered_set<int> st2(prop[j].begin(), prop[j].end());

                if (intersect(st1, st2) >= k) {
                    Union(i, j);
                }
            }
        }

        unordered_set<int> res;
        for (int i = 0; i < n; i++) {
            res.insert(find(i));
        }

        return res.size();
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
        if (parent[n] != n) {
            parent[n] = find(parent[n]);
        }
        return parent[n];
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