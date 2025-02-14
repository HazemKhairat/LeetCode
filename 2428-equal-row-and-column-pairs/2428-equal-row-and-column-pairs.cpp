class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        int n = grid.size(), count = 0;
        vector<int> row(n), col(n);
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < n; k++) {
                row[k] = grid[i][k];
            }
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    col[k] = grid[k][j];
                }
                if (row == col)
                    count++;
            }
        }
        return count;
    }
};