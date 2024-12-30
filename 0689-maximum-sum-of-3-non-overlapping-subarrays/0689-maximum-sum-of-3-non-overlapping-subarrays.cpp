class Solution {
public:
    vector<vector<long>> memo;
    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        int n = nums.size() - k + 1;
        memo = vector<vector<long>>(n, vector<long>(4, -1));
        vector<int> sum(n, 0);
        int window = 0;
        for (int i = 0; i < k; i++) {
            window += nums[i];
        }
        sum[0] = window;
        for (int i = k; i < nums.size(); i++) {
            window = window - nums[i - k] + nums[i];
            sum[i - k + 1] = window;
        }
        ComputMemo(sum, 3, 0, k);
        vector<int> res;
        dfs(sum, 3, 0, k, res);
        return res;
    }

    int ComputMemo(vector<int>& sum, int arrIdx, int sumIdx, int k) {
        if (arrIdx == 0) {
            return 0;
        }
        if (sumIdx >= sum.size()) {
            return arrIdx ? INT_MIN : 0;
        }
        if(memo[sumIdx][arrIdx] != -1){
            return memo[sumIdx][arrIdx];
        }
        int get = sum[sumIdx] + ComputMemo(sum, arrIdx - 1, sumIdx + k, k);
        int skip = ComputMemo(sum, arrIdx, sumIdx + 1, k);
        return memo[sumIdx][arrIdx] = max(get, skip);
    }

    void dfs(vector<int>& sum, int arrIdx, int sumIdx, int k,
             vector<int>& res) {
        if (arrIdx == 0) {
            return;
        }
        if (sumIdx >= sum.size()) {
            return;
        }
        int get = sum[sumIdx] + ComputMemo(sum, arrIdx - 1, sumIdx + k, k);
        int skip = ComputMemo(sum, arrIdx, sumIdx + 1, k);

        if (get >= skip) {
            res.push_back(sumIdx);
            dfs(sum, arrIdx - 1, sumIdx + k, k, res);
        } else {
            dfs(sum, arrIdx, sumIdx + 1, k, res);
        }
    }
};