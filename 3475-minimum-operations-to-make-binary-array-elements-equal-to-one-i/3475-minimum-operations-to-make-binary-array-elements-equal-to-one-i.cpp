class Solution {
public:
    int minOperations(vector<int>& nums) {
        int res = 0;
        for (int i = 0; i < nums.size() - 2; i++) {
            if (nums[i] == 0) {
                res++;
                for (int j = i; j < (i + 3); j++) {
                    nums[j] ^= 1;
                }
            }
        }
        for (int num : nums) {
            if (!num) {
                return -1;
            }
        }
        cout << endl;
        return res;
    }
};