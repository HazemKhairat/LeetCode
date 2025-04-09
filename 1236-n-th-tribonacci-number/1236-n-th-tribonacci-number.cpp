class Solution {
public:
    int tribonacci(int n) {
        /*
        formula:
                - T[n] = T[n - 1] + T[n - 2] + T[n - 3];
        ex :
        n = 4

        0 1 2 3 4
        0 1 1 2 4
        */

        if (n < 3) {
            return n == 0 ? 0 : 1;
        }
        vector<int> dp(n + 1);
        dp[0] = 0, dp[1] = 1, dp[2] = 1;

        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
        }

        return dp[n];
    }
};