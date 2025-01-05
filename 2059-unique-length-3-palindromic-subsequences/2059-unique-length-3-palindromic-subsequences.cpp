class Solution {
public:
    int countPalindromicSubsequence(string s) {
        set<char> chars(s.begin(), s.end());
        int ans = 0;
        for (auto ch : chars) {
            int firstPos = -1, lastPos = -1;
            for (int i = 0; i < s.size(); i++) {
                if (ch == s[i]) {
                    if (firstPos == -1) {
                        firstPos = i;
                    }
                    lastPos = i;
                }
            }

            set<char> mid;
            for (int k = firstPos + 1; k < lastPos; k++) {
                mid.insert(s[k]);
            }
            ans += mid.size();
        }

        return ans;
    }
};