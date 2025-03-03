class Solution {
public:
    map<pair<int, int>, int> memo;
    int longestPalindromeSubseq(string s) { return solve(s, 0, s.size() - 1); }

    int solve(string& s, int i, int j) {
        if (i > j) {
            return 0;
        }
        if (i == j) {
            return 1;
        }
        if (memo.count({i, j})) {
            return memo[{i, j}];
        }

        if (s[i] == s[j]) {
            memo[{i, j}] = 2 + solve(s, i + 1, j - 1);
        } else {
            int left = solve(s, i + 1, j);
            int right = solve(s, i, j - 1);
            memo[{i, j}] = max(left, right);
        }

        return memo[{i, j}];
    }
};