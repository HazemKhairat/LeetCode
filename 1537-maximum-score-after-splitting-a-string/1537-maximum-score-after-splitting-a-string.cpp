class Solution {
public:
    int maxScore(string s) {
        int zeros = 0, ones = count(s.begin(), s.end(), '1'),
            res = 0, pointer = 0;
        while (pointer < s.size() - 1) {
            if (s[pointer] == '1') {
                ones--;
            } else {
                zeros++;
            }
            res = max(res, ones + zeros);
            pointer++;
        }
        return res;
    }
};