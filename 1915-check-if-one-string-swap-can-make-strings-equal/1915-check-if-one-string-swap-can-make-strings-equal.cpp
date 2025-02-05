class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        map<int, int> freq1, freq2;
        int count = 0;
        for (int i = 0; i < s1.size(); i++) {
            freq1[s1[i]]++;
            freq2[s2[i]]++;
            if (s1[i] != s2[i]) {
                count++;
                if (count > 2) {
                    return false;
                }
            }
        }

        for (int i = 0; i < s1.size(); i++) {
            if (freq1[s1[i]] != freq2[s1[i]]) {
                return false;
            }
        }

        return true;
    }
};