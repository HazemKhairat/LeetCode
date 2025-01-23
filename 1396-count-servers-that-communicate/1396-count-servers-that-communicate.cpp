class Solution {
public:
    vector<vector<bool>> visited;
    int countServers(vector<vector<int>>& grid) {
        visited = vector<vector<bool>>(255, vector<bool>(255, false));
        int n = grid.size(), m = grid[0].size();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if(grid[i][j] == 1){
                    ans++;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if(grid[i][j] == 0){
                    continue;
                }
                bool isolated = true;
                int left, right, top, bottom;
                for(left = j - 1; left >= 0; left--){
                    if(grid[i][left] == 1){
                        isolated = false;
                    }
                }

                for(right = j + 1; right < m; right++){
                    if(grid[i][right] == 1){
                        isolated = false;
                    }
                }

                for(top = i - 1; top >= 0; top--){
                    if(grid[top][j] == 1){
                        isolated = false;
                    }
                }

                for(bottom = i + 1; bottom < n; bottom++){
                    if(grid[bottom][j] == 1){
                        isolated = false;
                    }
                }

                if(isolated){
                    ans--;
                }
            }
        }

        return ans;
    }
};