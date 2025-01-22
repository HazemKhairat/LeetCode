class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int n = mat.size(), m = mat[0].size();
        vector<vector<int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        vector<vector<int>> res(n, vector<int>(m, 0));
        vector<vector<bool>> visited(n, vector<bool>(m, false));
        priority_queue<vector<int>, vector<vector<int>>, greater<>> pq;

        for (int row = 0; row < n; row++) {
            for (int col = 0; col < m; col++) {
                if (mat[row][col] == 0) {
                    visited[row][col] = true;
                    pq.push({0, row, col});
                }
            }
        }

        while (!pq.empty()) {
            auto curr = pq.top();
            pq.pop();
            int dist = curr[0], row = curr[1], col = curr[2];
            for (auto dir : dirs) {
                int newRow = row + dir[0];
                int newCol = col + dir[1];
                if (newRow < 0 || newCol < 0 || newRow == n || newCol == m ||
                    visited[newRow][newCol]) {
                    continue;
                } else {
                    res[newRow][newCol] = dist + 1;
                    pq.push({dist + 1, newRow, newCol});
                    visited[newRow][newCol] = true;
                }
            }
        }

        return res;
    }
};