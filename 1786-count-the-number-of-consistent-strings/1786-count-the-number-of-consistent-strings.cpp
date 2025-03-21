class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int allow = 0;
        for (char& ch : allowed) {
            allow |= (1 << (ch - 'a'));
        }

        int count = 0;
        for (string& word : words) {
            int tmp = 0;
            for (char& ch : word) {
                tmp |= (1 << (ch - 'a'));
            }
            if ((allow & tmp) == tmp) {
                count++;
            }
        }
        return count;
    }
};