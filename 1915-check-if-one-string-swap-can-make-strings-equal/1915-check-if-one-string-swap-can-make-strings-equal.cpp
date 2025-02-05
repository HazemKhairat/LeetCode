class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        // check anagram
        map<int, int> freq1, freq2;
        for (int i = 0; i < s1.size(); i++) {
            freq1[s1[i]]++;
            freq2[s2[i]]++;
        }
        for (int i = 0; i < s1.size(); i++) {
            if (freq1[s1[i]] != freq2[s1[i]]) {
                return false;
            }
        }

        // is it possible to make both strings equal by performing at most one
        // string swap on exactly one of the strings
        int count = 0;
        for (int i = 0; i < s1.size(); i++) {
            if (s1[i] != s2[i]) {
                count++;
            }
        }
        return count <= 2;
    }
};