class Solution {
public: //   0       1        2        3
    vector<vector<int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    int minCost(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        deque<vector<int>> dq;
        dq.push_front({0, 0, 0}); // cost , row, col
        vector<vector<int>> minCost(n, vector<int>(m, INT_MAX));
        minCost[0][0] = 0;

        while (!dq.empty()) {
            vector<int> curr = dq.front();
            dq.pop_front();
            int cost = curr[0], row = curr[1], col = curr[2];

            for (int dir = 0; dir < 4; dir++) {
                int newRow = row + dirs[dir][0];
                int newCol = col + dirs[dir][1];

                if (newRow >= 0 && newCol >= 0 && newRow < n && newCol < m) {
                    int newCost = cost + (grid[row][col] - 1 != dir);
                    if (newCost < minCost[newRow][newCol]) {
                        if (newCost == cost) {
                            dq.push_front({newCost, newRow, newCol});
                        } else {
                            dq.push_back({newCost, newRow, newCol});
                        }
                        minCost[newRow][newCol] = newCost;
                    }
                }
            }
        }

        return minCost[n - 1][m - 1];
    }
};