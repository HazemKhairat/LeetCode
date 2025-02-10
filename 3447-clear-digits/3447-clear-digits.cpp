class Solution {
public:
    string clearDigits(string s) {
        stack<char> st;
        for (int i = 0; i < s.size(); i++) {
            if (!st.empty() && isdigit(s[i])) {
                st.pop();
            } else {
                st.push(s[i]);
            }
        }

        string res;
        while (!st.empty()) {
            res.push_back(st.top());
            st.pop();
        }

        reverse(res.begin(), res.end());
        return res;
    }
};