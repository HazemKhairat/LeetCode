class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        int n = nums.size();

        vector<int> maxLeft(n), maxRight(n);
        for (int i = 1; i < n; i++) {
            maxLeft[i] = max(maxLeft[i - 1], nums[i - 1]);
            maxRight[n - i - 1] = max(maxRight[n - i], nums[n - i]);
        }

        long long maxi = 0;
        for (int j = 1; j < n; j++) {
            maxi = max(maxi, (long long)(maxLeft[j] - nums[j]) * maxRight[j]);
        }

        return maxi;
    }
};