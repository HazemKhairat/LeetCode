class Solution {
public:
    vector<vector<int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    int minCost(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        priority_queue<vector<int>, vector<vector<int>> , greater<>> pq;
        pq.push({0, 0, 0}); // row, col, cost
        vector<vector<int>> minCost(n, vector<int>(m, INT_MAX));
        minCost[0][0] = 0;

        while(!pq.empty()){
            vector<int> curr = pq.top();
            pq.pop();
            int cost = curr[0], row = curr[1], col = curr[2];

            if(minCost[row][col] != cost) continue;

            for(int dir = 0; dir < 4; dir++){
                int newRow = row + dirs[dir][0];
                int newCol = col + dirs[dir][1];

                if(newRow >= 0 && newRow < n && newCol >= 0 && newCol < m){
                    int newCost = cost + (dir != (grid[row][col] - 1) ? 1 : 0);

                    if(minCost[newRow][newCol] > newCost){
                        minCost[newRow][newCol] = newCost;
                        pq.push({newCost, newRow, newCol});
                    }
                }
            }
        }

        return minCost[n - 1][m - 1];

    }
};