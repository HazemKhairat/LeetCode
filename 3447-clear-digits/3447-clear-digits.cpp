class Solution {
public:
    string clearDigits(string s) {
        for (int i = 1; i < s.size(); i++) {
            if (isdigit(s[i])) {
                for (int j = i; j >= 0; j--) {
                    if (!isdigit(s[j]) && s[j] != ' ') {
                        s[j] = ' ';
                        break;
                    }
                }
            }
        }

        string res = "";
        for (char ch : s) {
            if (!isdigit(ch) && ch != ' ') {
                res.push_back(ch);
            }
        }
        return res;
    }
};