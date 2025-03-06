class Solution {
public:
    vector<vector<int>> memo;
    int maxProfit(vector<int>& prices, int fee) {
        memo = vector<vector<int>>(2, vector<int>(prices.size() + 5));
        return solve(prices, fee, 0, 1);
    }

    int solve(vector<int>& prices, int& fee, int index, bool buy) {
        if (index >= prices.size()) {
            return 0;
        }
        if (memo[buy][index]) {
            return memo[buy][index];
        }
        int profit = 0;

        if (buy) {
            int take = -prices[index] + solve(prices, fee, index + 1, 0);
            int skip = solve(prices, fee, index + 1, 1);
            profit = max(take, skip);
        } else {
            int sell = prices[index] - fee + solve(prices, fee, index + 1, 1);
            int skip = solve(prices, fee, index + 1, 0);
            profit = max(sell, skip);
        }

        return memo[buy][index] = profit;
    }
};