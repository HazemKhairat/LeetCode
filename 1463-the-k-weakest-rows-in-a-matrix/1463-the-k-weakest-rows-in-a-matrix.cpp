class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        vector<pair<int, int>> v;
        for (int i = 0; i < mat.size(); i++) {
            int numOfones = lowerBound(mat[i]);
            v.push_back({i, numOfones});
        }

        sort(v.begin(), v.end(), [](pair<int, int>& a, pair<int, int>& b) {
            return a.second < b.second || (a.second == b.second && a.first < b.first);
        });

        vector<int> res;
        for (int i = 0; i < k; i++) {
            res.push_back(v[i].first);
        }

        return res;
    }

    int lowerBound(vector<int> row) {
        int l = 0, r = row.size() - 1, index = row.size();
        while (l <= r) {
            int mid = (l + r) / 2;
            if (row[mid] == 0) {
                r = mid - 1;
                index = mid;
            } else {
                l = mid + 1;
            }
        }

        return index;
    }
};