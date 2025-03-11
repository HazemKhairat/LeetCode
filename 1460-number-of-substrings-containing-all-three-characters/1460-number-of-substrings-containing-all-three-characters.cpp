class Solution {
public:
    int numberOfSubstrings(string s) {
        int res = 0;
        unordered_map<char, int> freq;
        int i = 0, j = 0;

        while (j < s.size()) {
            freq[s[j]]++;

            while (i < j && freq.size() == 3) {
                res += s.size() - j;
                if(--freq[s[i]] == 0) freq.erase(s[i]);
                i++;
            }
            j++;
        }

        return res;
    }
};