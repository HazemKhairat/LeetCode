class Solution {
public:
    int sum;
    int numEnclaves(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1) {
                    sum = 0;
                    if (dfs(grid, i, j)) {
                        res += sum;
                    }
                }
            }
        }

        return res;
    }

    bool dfs(vector<vector<int>>& grid, int i, int j) {
        if (i < 0 || j < 0 || i == grid.size() || j == grid[0].size()) {
            return false;
        }
        if (grid[i][j] == 0) {
            return true;
        }
        if (grid[i][j] == 1) {
            grid[i][j] = 0;
            sum++;
        }
        bool up = dfs(grid, i + 1, j), down = dfs(grid, i - 1, j),
             right = dfs(grid, i, j + 1), left = dfs(grid, i, j - 1);
        return up && down && left && right;
    }
};