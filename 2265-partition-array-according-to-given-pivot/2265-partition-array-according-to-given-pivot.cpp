class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        int n = nums.size(), lessIdx = 0, greaterIdx = n - 1;
        vector<int> res(n);

        for (int i = 0, j = n - 1; i < n; i++, j--) {
            if (nums[i] < pivot) {
                res[lessIdx++] = nums[i];
            }
            if (nums[j] > pivot) {
                res[greaterIdx--] = nums[j];
            }
        }

        while (lessIdx <= greaterIdx) {
            res[lessIdx++] = pivot;
        }

        return res;
    }
};