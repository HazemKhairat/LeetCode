class Solution {
public:
    vector<vector<int>> memo;
    int numSquares(int n) {
        vector<int> nums;
        for (int i = 1; i * i <= n; i++) {
            nums.push_back(i * i);
        }
        memo = vector<vector<int>>(nums.size(), vector<int>(n + 1));
        return solve(n, nums, 0);
    }

    int solve(int n, vector<int>& nums, int index) {
        if (n == 0) {
            return 0;
        }
        if (index >= nums.size() || n < 0) {
            return 100000;
        }
        if (memo[index][n]) {
            return memo[index][n];
        }

        int take = 1 + solve(n - nums[index], nums, index);
        int skip = solve(n, nums, index + 1);

        return memo[index][n] = min(take, skip);
    }
};