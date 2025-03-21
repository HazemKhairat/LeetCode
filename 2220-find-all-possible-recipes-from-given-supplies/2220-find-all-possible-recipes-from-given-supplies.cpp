class Solution {
public:
    vector<string> findAllRecipes(vector<string>& recipes,
                                  vector<vector<string>>& ingredients,
                                  vector<string>& supplies) {
        unordered_set<string> available(supplies.begin(), supplies.end());
        vector<string> res;
        queue<int> q;
        for (int i = 0; i < recipes.size(); i++) {
            q.push(i);
        }
        int lastSize = 0;
        while (available.size() > lastSize) {
            lastSize = available.size();
            int size = q.size();
            while (size--) {
                int id = q.front();
                q.pop();
                bool ok = true;
                for (int i = 0; i < ingredients[id].size(); i++) {
                    if (!available.count(ingredients[id][i])) {
                        ok = false;
                        break;
                    }
                }
                if (!ok) {
                    q.push(id);
                } else {
                    res.push_back(recipes[id]);
                    available.insert(recipes[id]);
                }
            }
        }

        return res;
    }
};