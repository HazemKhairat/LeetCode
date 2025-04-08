class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int n = nums.size();
        int res = 0;
        for (int i = 0; i < n; i += 3) {
            unordered_set<int> distinct;
            bool valid = true;
            for (int j = i; j < n; j++) {
                if (distinct.count(nums[j])) {
                    valid = false;
                    break;
                }
                distinct.insert(nums[j]);
            }
            if (valid) {
                return res;
            }
            res++;
        }

        return res;
    }
};