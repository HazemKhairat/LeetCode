class Solution {
public:
    int numTilePossibilities(string tiles) {
        set<string> res;
        vector<bool> used(tiles.size() + 1, 0);
        backtrack(tiles, res, used, "");
        return res.size();
    }

    void backtrack(string& tiles, set<string>& res, vector<bool>& used,
                   string substr) {
        // cout << substr << endl;
        for (int i = 0; i < tiles.size(); i++) {
            if (used[i]) {
                continue;
            }
            substr.push_back(tiles[i]);
            res.insert(substr);
            used[i] = true;
            backtrack(tiles, res, used, substr);
            substr.pop_back();
            used[i] = false;
        }
    }
};