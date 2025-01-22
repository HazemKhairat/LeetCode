class Solution {
public:
    vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {
        vector<vector<int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int n = isWater.size(), m = isWater[0].size();

        vector<vector<bool>> visited(n, vector<bool>(m, false));
        vector<vector<int>> grid(n, vector<int>(m, 0));
        priority_queue<vector<int>, vector<vector<int>>, greater<>> pq;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (isWater[i][j]) {
                    visited[i][j] = true;
                    pq.push({0, i, j});
                }
            }
        }

        while(!pq.empty()){
            auto curr = pq.top();
            pq.pop();
            int hight = curr[0], row = curr[1], col = curr[2];

            for(auto dir : dirs){
                int newRow = row + dir[0];
                int newCol = col + dir[1];
                if(newRow < 0 || newRow == n || newCol < 0 || newCol ==m || visited[newRow][newCol]){
                    continue;
                }
                else{
                    grid[newRow][newCol] = hight + 1;
                    visited[newRow][newCol] = true;
                    pq.push({hight + 1, newRow, newCol});
                }
            }
        }

        return grid;
    }
};