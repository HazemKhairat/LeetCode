class Solution {
public:
    string removeOccurrences(string s, string part) {
        stack<char> stk;
        int strLen = s.length();
        int partLen = part.length();

        for (int i = 0; i < strLen; i++) {
            stk.push(s[i]);
            if (stk.size() >= partLen && checkMatch(stk, part, partLen)) {
                for (int j = 0; j < partLen; j++) {
                    stk.pop();
                }
            }
        }

        string res = "";
        while (!stk.empty()) {
            res = stk.top() + res;
            stk.pop();
        }

        return res;
    }

    bool checkMatch(stack<char>& stk, string& part, int partLen) {
        stack<char> tmp = stk;

        for (int partIdx = partLen - 1; partIdx >= 0; partIdx--) {
            if (tmp.top() != part[partIdx]) {
                return false;
            }
            tmp.pop();
        }

        return true;
    }
};