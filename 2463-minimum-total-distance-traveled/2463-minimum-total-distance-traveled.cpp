class Solution {
public:
    long long minimumTotalDistance(vector<int>& robot,
                                   vector<vector<int>>& factory) {
        sort(robot.begin(), robot.end());
        sort(factory.begin(), factory.end());

        vector<int> f_posi;
        for (auto f : factory) {
            for (int i = 0; i < f[1]; i++) {
                f_posi.push_back(f[0]);
            }
        }
        int n = robot.size(), m = f_posi.size();
        vector<vector<long long>> dp(n + 1, vector<long long>(m + 1));

        for (int i = 0; i < n; i++) {
            dp[i][m] = 1e12;
        }

        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                dp[i][j] =
                    min((abs(robot[i] - f_posi[j]) + dp[i + 1][j + 1]),
                        dp[i][j + 1]);
            }
        }

        return dp[0][0];
    }
};