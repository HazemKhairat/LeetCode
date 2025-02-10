class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int i = 0, j = 0, zeros = 0;
        while (j < nums.size()) {
            if (nums[j] == 0) {
                zeros++;
            }
            if(zeros > k) break;
            j++;
        }

        int maxWindow = j - i;

        while (j < nums.size()) {
            if (zeros > k) {
                if (nums[i] == 0) {
                    zeros--;
                }
                i++;
            } else {
                j++;
                if (j < nums.size() && nums[j] == 0) {
                    zeros++;
                }
            }
            maxWindow = max(maxWindow, j - i);
        }

        return maxWindow;
    }
};