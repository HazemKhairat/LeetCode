class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& h) {
        int Rows = h.size(), Cols = h[0].size();
        set<vector<int>> pac, atl;
        vector<vector<int>> res;
        for (int c = 0; c < Cols; c++) {
            dfs(0, c, h, h[0][c], pac);
            dfs(Rows - 1, c, h, h[Rows - 1][c], atl);
        }
        for (int r = 0; r < Rows; r++) {
            dfs(r, 0, h, h[r][0], pac);
            dfs(r, Cols - 1, h, h[r][Cols - 1], atl);
        }
        for (int r = 0; r < Rows; r++) {
            for (int c = 0; c < Cols; c++) {
                if (pac.count({r, c}) && atl.count({r, c})) {
                    res.push_back({r, c});
                }
            }
        }
        return res;
    }

    void dfs(int r, int c, vector<vector<int>>& h, int Prev,
             set<vector<int>>& visit) {
        if (r < 0 || c < 0 || r == h.size() || c == h[0].size() ||
            Prev > h[r][c] || visit.count({r, c}))
            return;
        visit.insert({r, c});
        dfs(r + 1, c, h, h[r][c], visit);
        dfs(r - 1, c, h, h[r][c], visit);
        dfs(r, c + 1, h, h[r][c], visit);
        dfs(r, c - 1, h, h[r][c], visit);
    }
};
