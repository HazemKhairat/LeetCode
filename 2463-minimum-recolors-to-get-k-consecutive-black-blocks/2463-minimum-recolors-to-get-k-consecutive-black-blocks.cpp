class Solution {
public:
    int minimumRecolors(string blocks, int k) {
        int left = 0, right = k - 1;
        int res = INT_MAX;

        while (right < blocks.size()) {
            int black = 0;
            for (int i = left; i <= right; i++) {
                if (blocks[i] == 'B') {
                    black++;
                }
            }
            res = min(res, k - black);
            left++, right++;
        }

        return res;
    }
};