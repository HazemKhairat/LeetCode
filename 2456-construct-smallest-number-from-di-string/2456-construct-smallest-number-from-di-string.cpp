class Solution {
public:
    string smallestNumber(string pattern) {
        // STK.PUSH(INDEX + 1) = [7]
        // 0 1 2 3 4 5 6
        // D D D D I I _ -> 6
        // 5 4 3 2 1 6 7

        string res;
        stack<int> stk;

        for (int i = 0; i <= pattern.size(); i++) {
            stk.push(i + 1);
            while ((i == pattern.size() || pattern[i] == 'I') && !stk.empty()) {
                res += ('0' + stk.top());
                stk.pop();
            }
        }

        return res;
    }
};