class Solution {
public:
    string smallestNumber(string pattern) {
        int n = pattern.size() + 1;
        vector<bool> used(n + 5, 0);
        string res = "";
        backtrack(0, res, used, n, pattern);
        return res;
    }

    void backtrack(int idx, string& res, vector<bool>& used, int n,
                   string pattern) {
        if (res.size() == n) {
            return;
        }
        for (int i = 1; i <= n; i++) {
            if (used[i]) {
                continue;
            }
            if (idx == 0 ||
                (pattern[idx - 1] == 'I' && (i + '0') > res.back()) ||
                (pattern[idx - 1] == 'D' && (i + '0') < res.back())) {
                used[i] = true;
                res.push_back(('0' + i));
                backtrack(idx + 1, res, used, n, pattern);
                if (res.size() == n)
                    return;
                used[i] = false;
                res.pop_back();
            }
        }
    }
};