class Solution {
public:
    string getHappyString(int n, int k) {
        vector<char> list = {'a', 'b', 'c'};
        vector<string> res;
        backtrack(list, res, "", n);
        return res.size() >= k ? res[k - 1] : "";
    }

    void backtrack(vector<char>& list, vector<string>& res, string subStr,
                   int n) {
        if (subStr.size() == n) {
            res.push_back(subStr);
            return;
        }

        for (int i = 0; i < 3; i++) {
            if (!subStr.empty() && subStr.back() == list[i]) {
                continue;
            }
            subStr.push_back(list[i]);
            backtrack(list, res, subStr, n);
            subStr.pop_back();
        }
    }
};