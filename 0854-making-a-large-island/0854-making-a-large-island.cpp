class Solution {
public:
    vector<vector<int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    int largestIsland(vector<vector<int>>& grid) {
        int n = grid.size();
        int land = 2;
        map<int, int> mp;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    // cout << dfs(grid, i, j, n, land) << endl;
                    mp[land] = dfs(grid, i, j, n, land);
                    land++;
                }
            }
        }

        int res = 0;
        for (auto item : mp) {
            res = max(res, item.second);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                set<int> visited;
                if (grid[i][j] == 0) {
                    int tmp = 1;
                    for (auto dir : dirs) {
                        int nr = i + dir[0];
                        int nc = j + dir[1];
                        if (!outOfBound(nr, nc, n) &&
                            !visited.count(grid[nr][nc])) {
                            tmp += mp[grid[nr][nc]];
                            visited.insert(grid[nr][nc]);
                        }
                    }
                    res = max(res, tmp);
                }
            }
        }
        return res;
    }

    int dfs(vector<vector<int>>& grid, int i, int j, int n, int land) {
        if (outOfBound(i, j, n) || grid[i][j] != 1) {
            return 0;
        }

        grid[i][j] = land;
        int res = 1;
        for (auto dir : dirs) {
            int nr = i + dir[0];
            int nc = j + dir[1];
            res += dfs(grid, nr, nc, n, land);
        }
        return res;
    }

    bool outOfBound(int i, int j, int n) {
        return i < 0 || j < 0 || i == n || j == n;
    }
};