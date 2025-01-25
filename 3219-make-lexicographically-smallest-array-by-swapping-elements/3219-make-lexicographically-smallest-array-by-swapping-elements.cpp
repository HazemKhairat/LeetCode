class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        vector<int> sortedNums(nums.begin(), nums.end());
        sort(sortedNums.begin(), sortedNums.end());
        map<int, int> map;
        vector<queue<int>> groups;
        int qNum = 0;

        for (int i = 0; i < nums.size();) {
            queue<int> q;
            while (i < nums.size() &&
                   (q.empty() || sortedNums[i] - q.back() <= limit)) {
                q.push(sortedNums[i]);
                map[sortedNums[i]] = qNum;
                i++;
            }
            groups.push_back(q);
            qNum++;
        }

        vector<int> res(nums.size(), 0);
        for (int i = 0; i < nums.size(); i++) {
            int groupNum = map[nums[i]];
            res[i] = groups[groupNum].front();
            groups[groupNum].pop();
        }

        return res;
    }
};