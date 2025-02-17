class Solution {
public:
    vector<int> constructDistancedSequence(int n) {
        vector<int> res(2 * n - 1, 0);
        set<int> used;
        backtrack(0, res, n, used);
        return res;
    }

    bool backtrack(int i, vector<int>& res, int n, set<int>& used) {
        if (i == res.size()) {
            return true;
        }
        for (int num = n; num >= 1; num--) {
            if (used.count(num)) {
                continue;
            }
            if (num > 1 && (i + num >= res.size() || res[i + num])) {
                continue;
            }

            used.insert(num);
            res[i] = num;
            if (num > 1) {
                res[i + num] = num;
            }

            int j = i + 1;
            while (j < res.size() && res[j]) {
                j++;
            }

            if (backtrack(j, res, n, used)) {
                return true;
            }

            used.erase(num);
            res[i] = 0;
            if (num > 1) {
                res[i + num] = 0;
            }
        }

        return false;
    }
};