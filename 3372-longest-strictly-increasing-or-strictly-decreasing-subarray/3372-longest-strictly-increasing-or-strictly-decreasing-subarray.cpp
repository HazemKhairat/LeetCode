class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int longest = 1, inc = 1, dec = 1;
        int n = nums.size();
        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                inc++;
            } else {
                inc = 1;
            }

            if (nums[i] < nums[i - 1]) {
                dec++;
            } else {
                dec = 1;
            }
            longest = max(longest, max(inc, dec));
        }

        return longest;
    }
};