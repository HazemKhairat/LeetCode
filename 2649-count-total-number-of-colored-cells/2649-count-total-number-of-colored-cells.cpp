class Solution {
public:
    long long coloredCells(int n) {
        long long curr = 1;
        for(int i = 2; i <= n; i++){
            curr = curr + (4 * (i - 1));
            // cout << curr << endl;
        }
        return curr;
    }
};