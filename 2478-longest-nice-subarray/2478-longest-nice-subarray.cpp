class Solution {
public:
    int longestNiceSubarray(vector<int>& nums) {
        int start = 0, end = 0, maxLen = 0, usedBits = 0;
        for (; end < nums.size(); end++) {
            while ((usedBits & nums[end]) != 0) {
                usedBits ^= nums[start];
                start++;
            }
            usedBits |= nums[end];                 
            maxLen = max(maxLen, end - start + 1); 
        }
        return maxLen;
    }
};