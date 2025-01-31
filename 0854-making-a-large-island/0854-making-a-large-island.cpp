class Solution {
public:
    vector<vector<int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    int largestIsland(vector<vector<int>>& grid) {
        int n = grid.size();
        int landNum = 2;
        unordered_map<int, int> islands;
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1) {
                    int res = dfs(grid, r, c, landNum);
                    islands[landNum] = res;
                    // cout << landNum << " => " << islands[landNum] << endl;
                    landNum++;
                }
            }
        }

        int res = 0;
        for (auto& item : islands) {
            res = max(res, item.second);
        }

        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 0) {
                    int tmp = 1;
                    unordered_set<int> visited;
                    for (auto dir : dirs) {
                        int nr = r + dir[0];
                        int nc = c + dir[1];
                        if (!outOfBound(nr, nc, n) &&
                            !visited.count(grid[nr][nc])) {
                            tmp += islands[grid[nr][nc]];
                            visited.insert(grid[nr][nc]);
                        }
                    }
                    res = max(res, tmp);
                }
            }
        }

        return res;
    }

    int dfs(vector<vector<int>>& grid, int r, int c, int land) {
        if (outOfBound(r, c, grid.size()) || grid[r][c] != 1) {
            return 0;
        }
        grid[r][c] = land;
        int res = 1;
        for (auto dir : dirs) {
            int nr = r + dir[0];
            int nc = c + dir[1];
            res += dfs(grid, nr, nc, land);
        }
        return res;
    }

    bool outOfBound(int r, int c, int n) {
        return (r < 0 || c < 0 || r == n || c == n);
    }
};