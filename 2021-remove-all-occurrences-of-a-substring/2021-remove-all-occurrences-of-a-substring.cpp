class Solution {
public:
    string removeOccurrences(string s, string part) {
        stack<char> stk;
        for (int i = 0; i < s.size(); i++) {
            stk.push(s[i]);
            if (stk.size() >= part.size()) {
                if (matching(part, stk)) {
                    int j = part.size();
                    while (!stk.empty() && j--) {
                        stk.pop();
                    }
                }
            }
        }

        string res = "";
        while (!stk.empty()) {
            res += stk.top();
            stk.pop();
        }

        reverse(res.begin(), res.end());
        return res;
    }

    bool matching(string& part, stack<char> tmp) {
        for (int i = part.size() - 1; i >= 0; i--) {
            if (tmp.top() == part[i]) {
                tmp.pop();
            } else {
                return false;
            }
        }

        return true;
    }
};