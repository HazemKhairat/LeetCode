class Solution {
public:
    bool canConstruct(string s, int k) {
        if (s.size() < k) {
            return false;
        }

        vector<int> chars(26);
        for (auto c : s) {
            int ch = c - 'a';
            chars[ch]++;
        }

        int odd = 0;
        for (int i = 0; i < 26; i++) {
            if (chars[i] % 2 == 1) {
                odd++;
            }
        }

        if (k < odd) {
            return false;
        } else {
            return true;
        }
    }
};