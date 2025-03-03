class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& mat) {
        int n = mat.size();

        for (int row = 1; row < n; row++) {
            for (int col = 0; col < n; col++) {
                int mini = mat[row - 1][col];
                if (col - 1 >= 0) {
                    mini = min(mini, mat[row - 1][col - 1]);
                }
                if (col + 1 < n) {
                    mini = min(mini, mat[row - 1][col + 1]);
                }

                mat[row][col] += mini;
            }
        }

        int res = mat[n - 1][0];
        for (int col = 1; col < n; col++) {
            res = min(res, mat[n - 1][col]);
        }

        return res;
    }
};