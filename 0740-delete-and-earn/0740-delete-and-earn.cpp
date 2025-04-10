class Solution {
public:
    unordered_map<int, int> points;
    int deleteAndEarn(vector<int>& nums) {
        /*  - could we convert it to house ropper problem ? Yes
            - How ?
            sorted nums = 2 2 3 3 3 4
            unique = 2 3 4
            points 2 3 4
                   4 9 4

            1 3 5
        */
        sort(nums.begin(), nums.end());
        vector<int> unique;
        unique.push_back(nums[0]);
        for (int num : nums) {
            points[num] += num;
            if (num != unique.back()) {
                unique.push_back(num);
            }
        }

        return solve(unique, 0);
    }

    int solve(vector<int>& unique, int index) {
        if (index >= unique.size()) {
            return 0;
        }

        int take = 0, skip = 0;

        if (index < unique.size() - 1 && unique[index] == unique[index + 1] - 1)
            take = points[unique[index]] + solve(unique, index + 2);
        else
            take = points[unique[index]] + solve(unique, index + 1);

        skip = solve(unique, index + 1);
        return max(take, skip);
    }
};