class Solution {
public:
    vector<int> closestPrimes(int left, int right) {
        vector<int> primes = get_primes(left, right);
        int min_diff = INT_MAX;
        vector<int> res(2, -1);
        for (int i = 1; i < primes.size(); i++) {
            if (primes[i] - primes[i - 1] < min_diff) {
                min_diff = primes[i] - primes[i - 1];
                res[0] = primes[i - 1];
                res[1] = primes[i];
            }
        }
        return res;
    }

    vector<int> get_primes(int left, int right) {
        vector<bool> primes(right + 1, true);
        vector<int> res;
        for (int p = 2; p * p <= right; p++) {
            if (primes[p]) {
                for (int i = p * p; i <= right; i += p) {
                    primes[i] = false;
                }
            }
        }

        for (int i = left; i < primes.size(); i++) {
            if (i != 1 && primes[i]) {
                res.push_back(i);
            }
        }

        return res;
    }
};