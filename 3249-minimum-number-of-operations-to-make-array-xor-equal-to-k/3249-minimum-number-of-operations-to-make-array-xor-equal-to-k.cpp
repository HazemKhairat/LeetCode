class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int x = 0;
        for (auto num : nums) {
            x ^= num;
        }
        if (x == k)
            return 0;

        int res = 0;
        while (x || k) {
            if ((x & 1) != (k & 1)) {
                res++;
            }
            x >>= 1;
            k >>= 1;
        }
        return res;
    }
};