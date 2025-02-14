class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        int n = grid.size(), count = 0;
        map<vector<int>, int> mp;
        for (int i = 0; i < n; i++) {
            mp[grid[i]]++;
        }

        for (int i = 0; i < n; i++) {
            vector<int> v;
            for (int j = 0; j < n; j++) {
                v.push_back(grid[j][i]);
            }
            count += mp[v];
        }
        
        return count;
    }
};