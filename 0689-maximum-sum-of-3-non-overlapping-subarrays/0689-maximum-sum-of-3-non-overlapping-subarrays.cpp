class Solution {
public:
    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> prefx(n + 1, 0);
        for (int i = 1; i <= n; i++) {
            prefx[i] = prefx[i - 1] + nums[i - 1];
        }

        vector<vector<int>> dpSum(4, vector<int>(n + 1));
        vector<vector<int>> dpIndex(4, vector<int>(n + 1));

        for (int arr = 1; arr <= 3; arr++) {
            for (int idx = k; idx <= n; idx++) {
                int currSum =
                    dpSum[arr - 1][idx - k] + (prefx[idx] - prefx[idx - k]);
                if (currSum > dpSum[arr][idx - 1]) {
                    dpSum[arr][idx] = currSum;
                    dpIndex[arr][idx] = idx - k;
                } else {
                    dpSum[arr][idx] = dpSum[arr][idx - 1];
                    dpIndex[arr][idx] = dpIndex[arr][idx - 1];
                }
            }
        }

        vector<int> res(3);
        for (int arr = 3; arr >= 1; arr--) {
            int bestIdx = dpIndex[arr][n];
            res[arr - 1] = bestIdx;
            n = bestIdx;
        }

        return res;
    }
};