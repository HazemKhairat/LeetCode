class Solution {
public:
    int cashe[201][20001] = {[0 ... 200] = {[0 ... 20000] = -1}};

    bool canPartition(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % 2 == 1)
            return false;
        return backtrack(nums, 0, sum / 2);
    }

    bool backtrack(vector<int>& nums, int index, int sum) {
        if (index == nums.size() || sum < 0) {
            return false;
        }
        if (cashe[index][sum] != -1) {
            return cashe[index][sum];
        }
        if (sum == 0) {
            return true;
        }

        bool take = backtrack(nums, index + 1, sum - nums[index]);
        bool skip = backtrack(nums, index + 1, sum);

        return cashe[index][sum] = take or skip;
    }
};