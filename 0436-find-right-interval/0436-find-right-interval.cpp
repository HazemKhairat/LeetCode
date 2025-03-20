class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        vector<pair<int, int>> starts;
        for (int i = 0; i < intervals.size(); i++) {
            starts.push_back({intervals[i][0], i});
        }
        sort(starts.begin(), starts.end());

        vector<int> res;
        for (auto interval : intervals) {
            int index = search(interval, starts);
            res.push_back(index);
        }
        return res;
    }

    int search(vector<int>& interval, vector<pair<int, int>>& starts) {
        int left = 0, right = starts.size();
        while (left < right) {
            int mid = (left + right) / 2;
            if (starts[mid].first < interval[1]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left >= starts.size() ? -1 : starts[left].second;
    }
};