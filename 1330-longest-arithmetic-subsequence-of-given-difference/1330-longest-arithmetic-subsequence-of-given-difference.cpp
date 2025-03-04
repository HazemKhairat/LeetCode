class Solution {
public:
    int longestSubsequence(vector<int>& arr, int diff) {
        map<int, int> dp;
        int res = 1;
        
        for(int i = 0; i < arr.size(); i++){
            if(dp.count(arr[i] - diff)){
                dp[arr[i]] = 1 + dp[arr[i] - diff];
            }
            else{
                dp[arr[i]] = 1;
            }
            res = max(res, dp[arr[i]]);
        }

        return res;
    }
};