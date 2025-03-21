class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        vector<vector<int>> subsets;
        vector<int> sub;
        backtrack(nums, 0, subsets, sub);
        int total = 0;
        for (auto subset : subsets) {
            int currSum = 0;
            for (int i = 0; i < subset.size(); i++) {
                currSum ^= subset[i];
            }
            total += currSum;
        }
        return total;
    }

    void backtrack(vector<int>& nums, int index, vector<vector<int>>& subsets,
                   vector<int>& subset) {
        if (index == nums.size()) {    // index = 3 then push and return
            subsets.push_back(subset); // [5, 1, 6] , [5, 1], [5,6], [5], [1, 6]
            return;
        }
        cout << index << endl;
        // 0 , 1
        // subset = [1, 6
        subset.push_back(nums[index]);
        backtrack(nums, index + 1, subsets, subset); // 0 -> 2 -> 3
        subset.pop_back();
        backtrack(nums, index + 1, subsets, subset); // 1
    }
};