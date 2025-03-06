class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        int n = grid.size();

        set<int> st;
        for (int i = 1; i <= (n * n); i++) {
            st.insert(i);
        }

        vector<int> ans(2);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (st.count(grid[i][j])) {
                    st.erase(grid[i][j]);
                } else {
                    ans[0] = grid[i][j];
                }
            }
        }
        ans[1] = *st.begin();

        return ans;
    }
};