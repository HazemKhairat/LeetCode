class Solution {
public:
    string removeStars(string s) {
        stack<char> stack;
        for (auto ch : s) {
            if (ch == '*')
                stack.pop();
            else
                stack.push(ch);
        }

        string res = "";
        while (!stack.empty()) {
            res += stack.top();
            stack.pop();
        }
        reverse(res.begin(), res.end());
        return res;
    }
};