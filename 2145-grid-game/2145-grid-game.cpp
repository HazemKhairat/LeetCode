class Solution {
public:
    long long gridGame(vector<vector<int>>& grid) {
        int n = grid[0].size();
        vector<long long> pref(n, 0), suff(n, 0);
        pref[0] = grid[0][0], suff[n - 1] = grid[1][n - 1];

        for (int i = 1; i < n; i++) {
            pref[i] += grid[0][i] + pref[i - 1];
            suff[n - i - 1] += grid[1][n - i - 1] + suff[n - i];
        }

        long long res = LLONG_MAX;
        for (int i = 0; i < n; i++) {
            long long topSum = pref[n - 1] - pref[i];
            long long bottomSum = suff[0] - suff[i];
            long long secondRopot = max(topSum, bottomSum);
            res = min(res, secondRopot);
        }

        return res;
    }
};