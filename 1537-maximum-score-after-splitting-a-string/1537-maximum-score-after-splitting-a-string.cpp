class Solution {
public:
    int maxScore(string s) {
        int zeros = (s[0] == '0');
        int ones = 0;
        for (int i = 1; i < s.size(); i++) {
            ones += (s[i] == '1');
        }
        int res = ones + zeros;
        int pointer = 1;
        while (pointer < s.size() - 1) {
            if (s[pointer] == '1' && ones > 0) {
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