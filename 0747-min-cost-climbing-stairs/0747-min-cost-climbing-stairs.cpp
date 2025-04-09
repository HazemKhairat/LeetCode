class Solution {
public:
    vector<vector<int>> dp;
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        dp = vector<vector<int>>(n, vector<int>(n, -1));
        return solve(cost, 1, 0);
    }

    int solve(vector<int>& cost, int index, int step) {
        if (index >= cost.size()) {
            return 0;
        }
        if (dp[index][step] != -1) {
            return dp[index][step];
        }
        int one = cost[index - 1] + solve(cost, index + 1, step + 1);
        int two = cost[index] + solve(cost, index + 2, step + 1);

        return dp[index][step] = min(one, two);
    }
};