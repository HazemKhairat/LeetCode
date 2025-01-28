class Solution {
public:
    int findMaxFish(vector<vector<int>>& grid) {
        int res = 0;
        int n = grid.size(), m = grid[0].size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] > 0) {
                    res = max(res, bfs(grid, grid[i][j], i, j, n, m));
                }
            }
        }
        return res;
    }

    int bfs(vector<vector<int>>& grid, int cell, int i, int j, int n, int m) {
        queue<pair<int, int>> q;
        int maxi = 0;
        vector<vector<int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        q.push({i, j});
        while (!q.empty()) {
            auto curr = q.front();
            q.pop();
            int row = curr.first, col = curr.second;
            maxi += grid[row][col];
            grid[row][col] = 0;
            for (auto dir : dirs) {
                int newRow = row + dir[0];
                int newCol = col + dir[1];
                if (newRow < 0 || newRow == n || newCol < 0 || newCol == m ||
                    grid[newRow][newCol] == 0) {
                    continue;
                }

                q.push({newRow, newCol});
            }
        }

        return maxi;
    }
};