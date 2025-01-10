class Solution {
public:
    vector<string> wordSubsets(vector<string>& words1, vector<string>& words2) {
        vector<string> res;
        vector<int> v1(26, 0);
        for (auto word : words2) {
            vector<int> tmp(26);
            for (auto ch : word) {
                tmp[ch - 'a']++;
                v1[ch - 'a'] = max(v1[ch - 'a'], tmp[ch - 'a']);
            }
        }

        for (auto word : words1) {
            vector<int> v2(26);
            for (auto ch : word) {
                v2[ch - 'a']++;
            }

            bool ok = true;
            for (int i = 0; i < v2.size(); i++) {
                if (v2[i] < v1[i]) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                res.push_back(word);
            }
        }
        return res;
    }
};