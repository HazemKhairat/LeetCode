class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int maxSum = 0, tmp = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] <= nums[i - 1]) {
                maxSum = max(maxSum, tmp);
                tmp = 0;
            }
            tmp += nums[i];
        }
        maxSum = max(maxSum, tmp);
        return maxSum;
    }
};