class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        int mod = 1000000007;
        vector<int> dp(high + 1);
        dp[0] = 1;
        for (int i = 1; i <= high; i++) {
            if (i - zero >= 0) {
                dp[i] += (dp[i - zero] % mod);
            }
            if (i - one >= 0) {
                dp[i] += (dp[i - one] % mod);
            }
        }

        long res = 0;
        for (int i = low; i <= high; i++) {
            res += dp[i];
            res %= mod;
        }
        return res;
    }
};