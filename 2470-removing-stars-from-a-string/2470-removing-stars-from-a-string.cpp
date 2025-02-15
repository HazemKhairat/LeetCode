class Solution {
public:
    string removeStars(string s) {
        vector<char> stack;
        for (auto ch : s) {
            if (ch == '*')
                stack.pop_back();
            else
                stack.push_back(ch);
        }

        return string(stack.begin(), stack.end());
    }
};