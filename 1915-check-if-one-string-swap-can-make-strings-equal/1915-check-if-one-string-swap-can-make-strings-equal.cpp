class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        for (int i = 0; i < s1.size(); i++) {
            for (int j = i; j < s1.size(); j++) {
                swap(s1[i], s1[j]);
                if (s1 == s2) {
                    return true;
                }
                swap(s1[i], s1[j]);
            }
        }

        return false;
    }
};