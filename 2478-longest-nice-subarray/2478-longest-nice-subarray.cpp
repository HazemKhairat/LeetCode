class Solution {
public:
    int longestNiceSubarray(vector<int>& nums) {
        int maxLen = 1;
        for (int start = 0; start < nums.size(); start++) {
            int currLen = 1;
            int bitMask = nums[start];
            for (int end = start + 1; end < nums.size(); end++) {
                if ((bitMask & nums[end]) == 0) {
                    bitMask |= nums[end];
                    currLen++;
                } else {
                    break;
                }
            }
            maxLen = max(maxLen, currLen);
        }
        return maxLen;
    }
};