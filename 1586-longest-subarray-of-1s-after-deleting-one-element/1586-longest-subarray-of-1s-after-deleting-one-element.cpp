class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int i = 0, j = 0, curr0Idx = -1, maxLen = 0;
        while (j < nums.size()) {
            if (nums[j] == 0) {
                i = curr0Idx + 1;
                curr0Idx = j;
            }
            j++;
            maxLen = max(maxLen, j - i);
        }
        return maxLen - 1;
    }
};