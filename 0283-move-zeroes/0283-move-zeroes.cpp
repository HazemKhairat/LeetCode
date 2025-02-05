class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        vector<int> tmp;
        int count = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                count++;
            } else {
                tmp.push_back(nums[i]);
            }
        }

        int i = 0;
        for (; i < tmp.size(); i++) {
            nums[i] = tmp[i];
        }

        while (count--) {
            nums[i] = 0;
            i++;
        }

        return;
    }
};