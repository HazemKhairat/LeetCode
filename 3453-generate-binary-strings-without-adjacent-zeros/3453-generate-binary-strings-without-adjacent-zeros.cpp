class Solution {
public:
    vector<string> res;
    vector<string> validStrings(int n) {
        backtrack(n, "", -1);
        return res;
    }

    void backtrack(int n, string str, int i) {
        // cout << str << " size -> " << str.size() << endl;
        if (str.size() > 1) {
            // cout << str[i] << " " << str[i - 1] << endl;
            if (str[i] == '0' && str[i - 1] == '0')
                return;
        }
        if (str.size() == n) {
            res.push_back(str);
            return;
        }

        backtrack(n, str + '0', i + 1);
        backtrack(n, str + '1', i + 1);
    }
};