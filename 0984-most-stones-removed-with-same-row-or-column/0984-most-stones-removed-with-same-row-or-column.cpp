class Solution {
public:
    int removeStones(vector<vector<int>>& stones) {
        for (int i = 0; i < stones.size(); i++) {
            Union(stones[i][0], ~stones[i][1]);
        }

        return stones.size() - islands;
    }

    map<int, int> mp;
    int islands = 0;

    int find(int x) {
        if (!mp.count(x)) {
            mp[x] = x;
            islands++;
        }
        if (x != mp[x]) {
            mp[x] = find(mp[x]);
        }

        return mp[x];
    }

    void Union(int a, int b) {
        a = find(a), b = find(b);
        // a = 2, b = 2
        if (a != b) {
            mp[a] = b;
            islands--;
        }
    }
};