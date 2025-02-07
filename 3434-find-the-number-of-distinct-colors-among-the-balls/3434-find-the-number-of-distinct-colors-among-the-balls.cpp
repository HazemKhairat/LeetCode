class Solution {
public:
    vector<int> queryResults(int limit, vector<vector<int>>& queries) {
        map<int, int> nums, colors;
        vector<int> res;

        for (auto q : queries) {
            int u = q[0], v = q[1];
            if (nums.count(u)) {
                colors[nums[u]]--;
                if (colors[nums[u]] == 0) {
                    colors.erase(nums[u]);
                }
            }
            nums[u] = v;
            colors[v]++;
            res.push_back(colors.size());
        }

        return res;
    }
};