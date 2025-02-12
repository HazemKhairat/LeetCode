class Solution {
public:
    int maximumSum(vector<int>& nums) {
        vector<int> sums(nums.size());
        for (int i = 0; i < nums.size(); i++) {
            int tmp = nums[i];
            while (tmp) {
                sums[i] += (tmp % 10);
                tmp /= 10;
            }
        }

        map<int, vector<int>> sameIdxs;
        for (int i = 0; i < sums.size(); i++) {
            sameIdxs[sums[i]].push_back(i);
        }

        int res = -1;
        for (auto item : sameIdxs) {
            for (int i = 0; i < item.second.size(); i++) {
                for (int j = i + 1; j < item.second.size(); j++) {
                    int currSum = nums[item.second[i]] + nums[item.second[j]];
                    res = max(res, currSum);
                }
            }
        }
        return res;
    }
};