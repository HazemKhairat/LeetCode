class Solution {
public:
    int shortestBridge(vector<vector<int>>& grid) {
        int n = grid.size();
        bool ok = false;
        int idx1 = 0, idx2 = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    dfs(grid, i, j);
                    idx1 = i, idx2 = j;
                    // cout << idx1 << " " << idx2 << endl;
                    ok = true;
                    break;
                }
            }
            if (ok) {
                break;
            }
        }

        // for(int i = 0; i < n; i++){
        //     for(int j = 0; j < n; j++){
        //         cout << grid[i][j] << " ";
        //     }
        //     cout << endl;
        // }

        int res = INT_MAX;
        vector<vector<bool>> visited(n, vector<bool>(n));
        vector<vector<int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        queue<vector<int>> q;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    q.push({i, j, 0});
                    visited[i][j] = true;
                }
            }
        }

        while (!q.empty()) {
            int row = q.front()[0], col = q.front()[1], cost = q.front()[2];
            if (grid[row][col] == 1) {
                res = min(cost, res);
            }
            q.pop();
            for (auto dir : dirs) {
                int newRow = row + dir[0];
                int newCol = col + dir[1];
                if (valid(newRow, newCol, n) && !visited[newRow][newCol]) {
                    visited[newRow][newCol] = true;
                    if (grid[newRow][newCol] == 0) {
                        grid[newRow][newCol] = 2;
                        q.push({newRow, newCol, cost + 1});
                    } else {
                        q.push({newRow, newCol, cost});
                    }
                    // cout << grid[newRow][newCol] << " => " << cost << endl;
                }
            }
        }

        return res;
    }

    void dfs(vector<vector<int>>& grid, int i, int j) {
        if (!valid(i, j, grid.size()) || grid[i][j] != 1) {
            return;
        }
        grid[i][j] = 2;
        dfs(grid, i + 1, j);
        dfs(grid, i - 1, j);
        dfs(grid, i, j + 1);
        dfs(grid, i, j - 1);
    }

    bool valid(int i, int j, int n) {
        return i >= 0 && j >= 0 && i < n && j < n;
    }
};