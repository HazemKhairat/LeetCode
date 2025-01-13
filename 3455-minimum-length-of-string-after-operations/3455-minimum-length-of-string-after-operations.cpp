class Solution {
public:
    int minimumLength(string s) {
        int res = 0;
        vector<int> freq(26);

        for (int i = 0; i < s.size(); i++) {
            freq[s[i] - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if (freq[i] == 0) {
                continue;
            } else if (freq[i] % 2 == 0) {
                res += 2;
            } else {
                res++;
            }
        }

        return res;
    }
};