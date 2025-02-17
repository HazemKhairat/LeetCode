class Solution {
public:
    int numTilePossibilities(string tiles) {
        set<string> res;
        set<int> used;
        backtrack(0, tiles, res, used, "");
        return res.size();
    }

    void backtrack(int idx, string& tiles, set<string>& res, set<int>& used,
                   string substr) {
        // cout << substr << endl;
        if (idx == tiles.size()) {
            return;
        }
        
        for (int i = 0; i < tiles.size(); i++) {
            if (used.count(i)) {
                continue;
            }
            substr.push_back(tiles[i]);
            res.insert(substr);
            used.insert(i);
            backtrack(idx + 1, tiles, res, used, substr);
            substr.pop_back();
            used.erase(i);
        }
    }
};