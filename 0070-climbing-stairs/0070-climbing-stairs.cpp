class Solution {
public:
    int climbStairs(int n) {
        /*
        n = 5 , res -> 8
        dp 0 1 2 3 4 5
           1 1 2 3 5 8
        */

        int first = 1, second = 1, res = 0;

        for (int i = 2; i <= n; i++) {
            res = first + second;
            first = second;
            second = res;
        }

        return n > 1 ? res : 1;
    }
};