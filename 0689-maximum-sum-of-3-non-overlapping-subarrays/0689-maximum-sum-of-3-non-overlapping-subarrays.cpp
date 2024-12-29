class Solution {
public:
    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> prefixSum(n + 1, 0);

        for (int i = 1; i <= n; i++) {
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1];
        }

        vector<vector<int>> bestSum(4, vector<int>(n + 1, 0));
        vector<vector<int>> bestIndex(4, vector<int>(n + 1, 0));

        for (int subarrayCount = 1; subarrayCount <= 3; subarrayCount++) {
            for (int endIndx = k * subarrayCount; endIndx <= n; endIndx++) {
                int currentSum = prefixSum[endIndx] - prefixSum[endIndx - k] +
                                 bestSum[subarrayCount - 1][endIndx - k];

                if (currentSum > bestSum[subarrayCount][endIndx - 1]) {
                    bestSum[subarrayCount][endIndx] = currentSum;
                    bestIndex[subarrayCount][endIndx] = endIndx - k;
                } else {
                    bestSum[subarrayCount][endIndx] =
                        bestSum[subarrayCount][endIndx - 1];
                    bestIndex[subarrayCount][endIndx] =
                        bestIndex[subarrayCount][endIndx - 1];
                }
            }
        }

        vector<int> res(3, 0);
        int currentEnd = n;

        for (int subarrayIndex = 3; subarrayIndex >= 1; subarrayIndex--) {
            res[subarrayIndex - 1] = bestIndex[subarrayIndex][currentEnd];
            currentEnd = res[subarrayIndex - 1];
        }
        return res;
    }
};