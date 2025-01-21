class Solution {
public:
    long long gridGame(vector<vector<int>>& grid) {
        int n = grid[0].size();
        vector<long long> pref(grid[0].begin(), grid[0].end()), suff(grid[1].begin(), grid[1].end());
        for (int i = 1; i < n; i++) {
            pref[i] += pref[i - 1];
            suff[n - i - 1] += suff[n - i];
        }

        int col = 0;
        long long res = LLONG_MAX;
        for (int col = 0; col < n; col++) {
            long long top = pref[n - 1] - pref[col];
            long long bottom = suff[0] - suff[col];
            res = min(res, max(top, bottom));
        }

        return res;
    }
};