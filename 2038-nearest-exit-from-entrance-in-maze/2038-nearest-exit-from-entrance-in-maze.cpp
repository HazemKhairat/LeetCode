class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        // n = rows and m = columns
        int n = maze.size(), m = maze[0].size();
        // all possiple paths we can move to
        vector<vector<int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        // mark the initial standing as visited
        maze[entrance[0]][entrance[1]] = '+';
        
        // ======================
        bool firstTime = true;
        queue<vector<int>> queue;
        queue.push({0, entrance[0], entrance[1]});
        // ======================

        while (!queue.empty()) {
            int row = queue.front()[1], col = queue.front()[2],
                level = queue.front()[0];

            if (!firstTime) {
                if (row == 0 || col == 0 || row == n - 1 || col == m - 1) {
                    return level;
                }
            }
            firstTime = false;

            queue.pop();
            for (auto dir : dirs) {
                int newRow = row + dir[0];
                int newCol = col + dir[1];
                if (newRow >= 0 && newCol >= 0 && newRow < n && newCol < m &&
                    maze[newRow][newCol] != '+') {
                    maze[newRow][newCol] = '+';
                    queue.push({level + 1, newRow, newCol});
                }
            }
        }

        return -1;
    }
};