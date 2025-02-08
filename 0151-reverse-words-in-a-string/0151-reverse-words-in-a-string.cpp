class Solution {
public:
    string reverseWords(string s) {
        string tmp = "";
        string res = "";
        for (int i = s.size() - 1; i >= 0; i--) {
            if (s[i] == ' ') {
                if (!tmp.empty()) {
                    reverse(tmp.begin(), tmp.end());
                    res += tmp;
                    res += ' ';
                    tmp = "";
                }
                continue;
            }
            tmp += s[i];
        }

        reverse(tmp.begin(), tmp.end());
        res += tmp;
        if (res.back() == ' ')
            res.pop_back();
        return res;
    }
};