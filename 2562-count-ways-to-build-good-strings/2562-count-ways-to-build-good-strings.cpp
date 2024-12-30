class Solution {
public:
    vector<int> dp;
    int mod = 1000000007;
    int countGoodStrings(int low, int high, int zero, int one) {
        dp = vector<int>(high + 1, -1);
        dp[0] = 1;

        int ans = 0;
        for(int end = low; end <= high; end++){
            ans += dfs(end, zero, one);
            ans %= mod;
        }
        return ans;
    }

    int dfs(int end, int zero, int one){
        int count = 0;
        if(dp[end] != -1){
            return dp[end];
        }
        if(end >= zero){
            count += dfs(end - zero, zero, one);
        }
        if(end >= one){
            count += dfs(end - one, zero, one);
        }
        return dp[end] = count % mod;
    }
};