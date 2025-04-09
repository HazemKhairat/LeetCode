class Solution {
public:
    int rob(vector<int>& nums) {
        /*
            0 1 2 3 4
            2 7 9 3 1

            prev = 2
            curr = 7

            formula max(curr, prev + nums[i])

            index = 4
            tmp = 1 + 11 or 11 = 12
            prev = 11
            curr = 12
        */
        if (nums.size() == 1) {
            return nums[0];
        }

        int prev = nums[0], curr = nums[1];

        for (int i = 2; i < nums.size(); i++) {
            int tmp = max(curr, prev + nums[i]);
            prev = max(prev, curr);
            curr = max(curr, tmp);
        }

        return max(prev, curr);
    }
};