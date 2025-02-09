class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        long long n = nums.size();
        long long totalPair = (n * (n - 1)) / 2;
        map<int, int> freq;
        for (int i = 0; i < n; i++) {
            freq[nums[i] - i]++;
        }

        long long goodPairs = 0;
        for (auto num : freq) {
            long long cnt = num.second;
            if (cnt >= 2) {
                goodPairs += ((cnt * (cnt - 1)) / 2);
            }
        }

        long long badPairs = totalPair - goodPairs;
        return badPairs;
    }
};