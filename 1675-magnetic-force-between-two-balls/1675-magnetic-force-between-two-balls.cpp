class Solution {
public:
    int maxDistance(vector<int>& pos, int m) {
        int n = pos.size();
        sort(pos.begin(), pos.end());
        int low = 1, high = pos[n - 1];

        while (low <= high) {
            int mid = (low + high) / 2;
            if (isValid(mid, pos, m)) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return high;
    }

    bool isValid(int mid, vector<int>& pos, int m) {
        int prev = pos[0];
        m--;
        for (int i = 1; i < pos.size(); i++) {
            int curr = pos[i];
            if (curr - prev >= mid) {
                prev = curr;
                m--;
            }
            if (m == 0) {
                return true;
            }
        }
        return false;
    }
};