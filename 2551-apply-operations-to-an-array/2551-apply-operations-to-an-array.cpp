class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        int i = 0, j = 1, zeros = 0;
        vector<int> res;
        
        while (j < nums.size()) {
            if (nums[i] == nums[j]) {
                nums[i] *= 2;
                nums[j] = 0;
            }
            if (nums[i])
                res.push_back(nums[i]);
            else
                zeros++;
            i++, j++;
        }

        if (nums[i])
            res.push_back(nums[i]);
        else
            zeros++;
        
        while (zeros--) {
            res.push_back(0);
        }

        return res;
    }
};