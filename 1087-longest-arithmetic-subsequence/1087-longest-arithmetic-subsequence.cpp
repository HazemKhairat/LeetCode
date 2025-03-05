class Solution {
public:
    int longestArithSeqLength(vector<int>& nums) {
        int n = nums.size();
        if (n == 2) {
            return n;
        }

        vector<unordered_map<int, int>> dp(n);
        int longest = 2, diff;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                diff = nums[i] - nums[j];
                dp[i][diff] = dp[j].count(diff) ? dp[j][diff] + 1 : 2;
                longest = max(longest, dp[i][diff]);
            }
        }

        return longest;
    }
};