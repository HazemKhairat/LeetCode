class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        /*
            8 8 10 10

            2 4 5 5 5

            1 2 2

            if(nums[0] < k)  return -1;
        */

        sort(nums.begin(), nums.end());
        if (nums[0] < k) {
            return -1;
        }

        unordered_set<int> operations;
        operations.insert(k);

        int res = 0;
        for (int num : nums) {
            if (operations.count(num) == 0) {
                res++;
            }
            operations.insert(num);
        }

        return res;
    }
};