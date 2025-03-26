class Solution {
public:
    vector<vector<bool>> vis;
    int closedIsland(vector<vector<int>>& grid) {
        /*
            - can we solve it dfs
            - if 0 we will dfs
            - for dirctions must be 1s
        */
        int n = grid.size(), m = grid[0].size(), res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 0) {
                    res += dfs(grid, i, j);
                }
            }
        }

        return res;
    }

    bool dfs(vector<vector<int>>& grid, int i, int j) {
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size()) {
            return false;
        }
        if (grid[i][j] == 1) {
            return true;
        }
        grid[i][j] = true;

        bool left = dfs(grid, i, j - 1), right = dfs(grid, i, j + 1),
             up = dfs(grid, i - 1, j), down = dfs(grid, i + 1, j);
        return left && right && up && down;
    }
};