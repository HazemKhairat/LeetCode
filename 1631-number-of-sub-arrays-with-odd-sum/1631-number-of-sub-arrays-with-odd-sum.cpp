class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        long long pref_sum = 0, odd_cnt = 0, even_cnt = 0, res = 0;
        const int MOD = 1e9 + 7;

        for (auto num : arr) {
            pref_sum += num;

            if (pref_sum % 2) {
                res += (even_cnt + 1);
                odd_cnt++;
            } else {
                res += odd_cnt;
                even_cnt++;
            }
        }

        return (res % MOD);
    }
};