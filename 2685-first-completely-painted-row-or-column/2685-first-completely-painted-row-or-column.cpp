class Solution {
public:
    int firstCompleteIndex(vector<int>& arr, vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        vector<pair<int, int>> mp((n * m) + 10);
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                mp[mat[i][j]] = {i, j};
            }
        }

        vector<int> rows(m, -1), cols(n, -1);
        for(int i = 0; i < arr.size(); i++){
            int row = mp[arr[i]].first;
            int col = mp[arr[i]].second;
            rows[row]++;
            cols[col]++;
            if(rows[row] == n - 1 || cols[col] == m - 1){
                return i;
            }
        }

        return 0;
    }
};