class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        int n = nums.size();

        for (int i = 0; i < n - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
        }

        int nonZeroIdx = 0;
        for (int idx = 0; idx < n; idx++) {
            if (nums[idx]) {
                nums[nonZeroIdx++] = nums[idx];
            }
        }

        while (nonZeroIdx < n) {
            nums[nonZeroIdx++] = 0;
        }

        return nums;
    }
};