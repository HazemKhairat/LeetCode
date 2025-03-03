class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        set<int> visited;
        vector<int> res;
        for (auto num : nums) {
            if (!visited.count(num) && num < pivot) {
                res.push_back(num);
            }
        }
        for (auto num : nums) {
            if (!visited.count(num) && num == pivot) {
                res.push_back(num);
            }
        }

        for (auto num : nums) {
            if (!visited.count(num) && num > pivot) {
                res.push_back(num);
            }
        }

        return res;
    }
};