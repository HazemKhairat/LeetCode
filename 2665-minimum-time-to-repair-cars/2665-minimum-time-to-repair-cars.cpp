class Solution {
public:
    long long repairCars(vector<int>& ranks, int cars) {
        long long minItem = *min_element(ranks.begin(), ranks.end());
        long long low = 1, high = minItem * cars * cars;
        while (low < high) {
            long long mid = (low + high) / 2;
            if (search(mid, ranks, cars)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    bool search(long long& mid, vector<int>& ranks, int& cars) {
        long long total = 0;
        for (int i = 0; i < ranks.size(); i++) {
            total += sqrt(mid / ranks[i]);
        }
        return total >= cars;
    }
};