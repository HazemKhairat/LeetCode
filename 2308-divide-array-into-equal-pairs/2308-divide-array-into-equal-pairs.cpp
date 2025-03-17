class Solution {
public:
    bool divideArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int i = 0, j = 1;
        while (j < nums.size()) {
            if (nums[i] != nums[j]) {
                return false;
            }
            i += 2;
            j += 2;
        }

        return true;
    }
};