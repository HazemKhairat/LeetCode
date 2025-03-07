class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        // n = rows and m = columns
        int n = maze.size(), m = maze[0].size();
        vector<vector<int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        vector<vector<bool>> visited(n, vector<bool>(m));
        visited[entrance[0]][entrance[1]] = true;
        queue<vector<int>> queue;
        queue.push({0, entrance[0], entrance[1]});
        while (!queue.empty()) {
            int row = queue.front()[1], col = queue.front()[2],
                level = queue.front()[0];
            if (!(row == entrance[0] && col == entrance[1])) {
                if (row == 0 || col == 0 || row == n - 1 || col == m - 1) {
                    return level;
                }
            }

            queue.pop();
            for (auto dir : dirs) {
                int newRow = row + dir[0];
                int newCol = col + dir[1];
                if (newRow >= 0 && newCol >= 0 && newRow < n && newCol < m &&
                    maze[newRow][newCol] != '+' && !visited[newRow][newCol]) {
                    visited[newRow][newCol] = true;
                    queue.push({level + 1, newRow, newCol});
                }
            }
        }

        return -1;
    }
};