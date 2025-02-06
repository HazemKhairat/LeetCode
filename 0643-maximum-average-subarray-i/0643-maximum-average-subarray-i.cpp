class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> pref(n + 1, 0);
        for (int i = 1; i <= n; i++) {
            pref[i] = nums[i - 1] + pref[i - 1];
        }

        double res = -1 * numeric_limits<double>::max();
        for (int i = 1; i <= (n - k) + 1; i++) {
            double curr = pref[i + k - 1] - pref[i - 1];
            res = max(res, (curr / k));
        }

        return res;
    }
};