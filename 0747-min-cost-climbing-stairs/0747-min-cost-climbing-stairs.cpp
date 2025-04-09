class Solution {
public:
    vector<int> dp;
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        dp = vector<int>(n, -1);
        return solve(cost, 1);
    }

    int solve(vector<int>& cost, int index) {
        if (index >= cost.size()) {
            return 0;
        }
        if (dp[index] != -1) {
            return dp[index];
        }
        int one = cost[index - 1] + solve(cost, index + 1);
        int two = cost[index] + solve(cost, index + 2);

        return dp[index] = min(one, two);
    }
};