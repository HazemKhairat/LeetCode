class Solution {
public:
    int countPalindromicSubsequence(string s) {
        set<char> chars(s.begin(), s.end());
        map<char, int> firstPos, lastPos;
        for (int i = 0; i < s.size(); i++) {
            if (!firstPos.count(s[i])) {
                firstPos[s[i]] = i;
            }
            lastPos[s[i]] = i;
        }

        int ans = 0;
        for (auto ch : chars) {
            int start = firstPos[ch] + 1, end = lastPos[ch] - 1;
            set<char> midChars;
            for (int i = start; i <= end; i++) {
                midChars.insert(s[i]);
            }
            ans += midChars.size();
        }

        return ans;
    }
};