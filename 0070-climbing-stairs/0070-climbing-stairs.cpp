class Solution {
public:
    vector<int> cashe;
    int climbStairs(int n) {
        cashe.resize(n + 1, -1);
        return dp(n);
    }

    int dp(int n) {
        if (n < 0) {
            return 0;
        }
        if (n == 0) {
            return 1;
        }
        if (cashe[n] != -1) {
            return cashe[n];
        }
        int one = 0, two = 0;
        one += dp(n - 1);
        two += dp(n - 2);
        return cashe[n] = one + two;
    }
};