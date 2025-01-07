class Solution {
public:
    vector<string> stringMatching(vector<string>& words) {
        vector<string> res;
        int n = words.size();
        for (int i = 0; i < n; i++) {
            string text = words[i];
            for (int j = 0; j < n; j++) {
                if (j == i)
                    continue;
                if (words[j].find(text) != string::npos) {
                    res.push_back(text);
                    break;
                }
            }
        }
        return res;
    }
};