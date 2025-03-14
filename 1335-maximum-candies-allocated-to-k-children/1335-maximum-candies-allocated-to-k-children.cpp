class Solution {
public:
    int maximumCandies(vector<int>& candies, long long k) {
        /* 1 - do binary search from 1 to sum / k
           2 - loop on candies arr to check if valid
        */
        long long sum = 0;
        for (auto candy : candies) {
            sum += candy;
        }
        if (sum < k) {
            return 0;
        }

        int left = 1, right = (sum / k);
        int res = 0;
        while (left <= right) {
            int mid = (left + right) / 2; // 3, 5, 6
            if (isValid(mid, candies, k)) {
                res = mid;
                left = mid + 1; // 1, 4, 6
            } else {
                right = mid - 1; // 6, 5
            }
        }

        return res;
    }

    bool isValid(int target, vector<int>& candies, long long k) {
        for (int i = 0; i < candies.size(); i++) {
            k = k - (candies[i] / target);
        }
        return k <= 0;
    }
};