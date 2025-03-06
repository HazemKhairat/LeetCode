class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int n = prices.size();
        vector<vector<int>> dp(n + 1, vector<int>(2));
        dp[n][0] = 0, dp[n][1] = 0;

        for (int idx = n - 1; idx >= 0; idx--) {
            for (int canBuy = 1; canBuy >= 0; canBuy--) {
                int buy = INT_MIN, sell = INT_MIN;
                if (canBuy) {
                    buy = -prices[idx] + dp[idx + 1][!canBuy];
                } else {
                    sell = prices[idx] - fee + dp[idx + 1][!canBuy];
                }
                int skip = dp[idx + 1][canBuy];
                dp[idx][canBuy] = max({buy, sell, skip});
            }
        }

        return dp[0][1];
    }
};