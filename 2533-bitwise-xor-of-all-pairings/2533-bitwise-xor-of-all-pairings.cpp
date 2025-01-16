class Solution {
public:
    int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size(), m = nums2.size();
        map<int, long long> freq;

        for (auto num : nums1) {
            freq[num] += m;
        }
        for (auto num : nums2) {
            freq[num] += n;
        }

        vector<int> nums3;
        for (auto item : freq) {
            if (item.second % 2 == 1) {
                nums3.push_back(item.first);
            }
        }

        int res = 0;
        for (auto item : nums3) {
            res ^= item;
        }

        return res;
    }
};