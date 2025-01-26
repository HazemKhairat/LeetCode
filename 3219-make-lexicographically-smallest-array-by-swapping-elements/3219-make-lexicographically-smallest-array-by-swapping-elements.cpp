class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        vector<int> sortedNums(nums.begin(), nums.end());
        sort(sortedNums.begin(), sortedNums.end());

        vector<queue<int>> groups;
        map<int, int> map;
        int qIndex = 0;

        for (int i = 0; i < nums.size();) {
            queue<int> q;
            while (i < nums.size() &&
                   (q.empty() || sortedNums[i] - q.back() <= limit)) {
                q.push(sortedNums[i]);
                map[sortedNums[i]] = qIndex;
                i++;
            }
            groups.push_back(q);
            qIndex++;
        }

        for (int i = 0; i < nums.size(); i++) {
            nums[i] = groups[map[nums[i]]].front();
            groups[map[nums[i]]].pop();
        }

        return nums;
    }
};