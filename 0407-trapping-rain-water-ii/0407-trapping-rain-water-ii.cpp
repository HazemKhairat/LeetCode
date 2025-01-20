class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        vector<vector<int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int n = heightMap.size(), m = heightMap[0].size();
        priority_queue<vector<int>, vector<vector<int>>, greater<>> pq;
        vector<vector<bool>> visited(n, vector<bool>(m, false));

        for (int i = 0; i < n; i++) {
            pq.push({heightMap[i][0], i, 0});
            pq.push({heightMap[i][m - 1], i, m - 1});
            visited[i][0] = visited[i][m - 1] = true;
        }

        for (int i = 0; i < m; i++) {
            pq.push({heightMap[0][i], 0, i});
            pq.push({heightMap[n - 1][i], n - 1, i});
            visited[0][i] = visited[n - 1][i] = true;
        }

        int res = 0;
        while (!pq.empty()) {
            auto curr = pq.top();
            pq.pop();
            int hight = curr[0], row = curr[1], col = curr[2];

            for (int dir = 0; dir < 4; dir++) {
                int newRow = row + dirs[dir][0];
                int newCol = col + dirs[dir][1];

                if (newRow < 0 || newCol < 0 || newRow == n || newCol == m ||
                    visited[newRow][newCol]) {
                    continue;
                }

                if (hight > heightMap[newRow][newCol]) {
                    res += (hight - heightMap[newRow][newCol]);
                    heightMap[newRow][newCol] = hight;
                }

                pq.push({heightMap[newRow][newCol], newRow, newCol});
                visited[newRow][newCol] = true;
            }
        }

        return res;
    }
};