class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        if (grid[0][0])
            return -1;
        vector<vector<int>> dirs = {{0, 1},  {0, -1}, {1, 0},  {-1, 0},
                                    {-1, 1}, {1, 1},  {1, -1}, {-1, -1}};
        queue<vector<int>> q;
        q.push({0, 0, 1}); // row, col, cost;
        vector<vector<bool>> vis(n, vector<bool>(n, false));
        vis[0][0] = true;

        while (!q.empty()) {
            int row = q.front()[0], col = q.front()[1], cost = q.front()[2];
            q.pop();
            // cout << row << " " << col << " " << cost << endl;
            if (row == n - 1 && col == n - 1) {
                return cost;
            }

            for (auto dir : dirs) {
                int newRow = row + dir[0];
                int newCol = col + dir[1];
                if (isValid(newRow, newCol, grid, vis)) {
                    q.push({newRow, newCol, cost + 1});
                    vis[newRow][newCol] = true;
                }
            }
        }

        return -1;
    }

    bool isValid(int i, int j, vector<vector<int>>& grid,
                 vector<vector<bool>>& vis) {
        return i >= 0 && j >= 0 && i < grid.size() && j < grid.size() &&
               !grid[i][j] && !vis[i][j];
    }
};