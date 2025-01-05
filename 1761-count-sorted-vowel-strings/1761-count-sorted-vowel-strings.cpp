class Solution {
public:
    int countVowelStrings(int n) {
        vector<int> dp = {0, 1, 1, 1, 1, 1};
        for(int i = 0; i < n; i++){
            for(int k = 1; k <= 5; k++){
                dp[k] += dp[k - 1];
            }
        }
        return dp[5];
    }
};