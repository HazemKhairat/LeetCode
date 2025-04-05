class Solution {
public:
    int subsetXORSum(vector<int>& nums) { return recurse(nums, 0, 0); }

    int recurse(vector<int>& nums, int index, int XorSum) {
        if (index == nums.size()) {
            return XorSum;
        }

        int take = recurse(nums, index + 1, XorSum ^ nums[index]);
        int skip = recurse(nums, index + 1, XorSum);

        return take + skip;
    }
};