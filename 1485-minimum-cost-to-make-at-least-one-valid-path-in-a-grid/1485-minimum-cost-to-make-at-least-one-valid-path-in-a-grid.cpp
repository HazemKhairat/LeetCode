class Solution {
public: // 0       1       2        3       4
    vector<vector<int>> dirs = {{0, 0}, {0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    int minCost(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        priority_queue<vector<int>, vector<vector<int>>, greater<>> pq;
        pq.push({0, 0, 0}); // cost, row, col
            vector<vector<int>>
                minCost(n, vector<int>(m, INT_MAX));
        minCost[0][0] = 0;

        while (!pq.empty()) {
            auto curr = pq.top();
            pq.pop();
            int cost = curr[0], row = curr[1], col = curr[2];

            for (int dir = 1; dir <= 4; dir++) {
                int newRow = row + dirs[dir][0];
                int newCol = col + dirs[dir][1];

                if (newRow < 0 || newCol < 0 || newRow == n || newCol == m) {
                    continue;
                }

                int newCost = cost + (grid[row][col] != dir);
                if (newCost < minCost[newRow][newCol]) {
                    minCost[newRow][newCol] = newCost;
                    pq.push({newCost, newRow, newCol});
                }
            }
        }

        return minCost[n - 1][m - 1];
    }
};