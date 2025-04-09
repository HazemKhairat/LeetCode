class Solution {
public:
    int fib(int n) {
        /*
            n = 6 , res = 8

            fib[n] = fib[n - 1] + fib[n - 2];
            0 1 2 3 4 5 6
            0 1 1 2 3 5 8
        */

        int prev = 0, curr = 1;
        for (int i = 2; i <= n; i++) {
            int tmp = prev + curr;
            prev = curr;
            curr = tmp;
        }

        return n >= 1 ? curr : 0;
    }
};