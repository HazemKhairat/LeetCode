class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        map<int, int> freq;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                int product = nums[i] * nums[j];
                freq[product]++;
            }
        }

        int res = 0;

        for (auto item : freq) {
            int count = item.second;
            if (count >= 2) {
                res += (count * (count - 1) / 2) * 8;
            }
        }
        return res;
    }
};