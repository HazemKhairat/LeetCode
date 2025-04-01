class Solution {
public:
    vector<long long> memo;

    long long mostPoints(vector<vector<int>>& questions) {
        int n = questions.size();
        memo = vector<long long>(n, -1);

        return dp(questions, 0);
    }

    long long dp(vector<vector<int>>& questions, int index) {
        if (index >= questions.size()) {
            return 0;
        }

        if (memo[index] != -1) {
            return memo[index];
        }

        long long solve = questions[index][0] +
                          dp(questions, index + questions[index][1] + 1);
        long long skip = dp(questions, index + 1);

        return memo[index] = max(solve, skip);
    }
};