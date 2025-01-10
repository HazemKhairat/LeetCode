class Solution {
public:
    vector<string> wordSubsets(vector<string>& words1, vector<string>& words2) {
        vector<string> res;
        vector<int> v2(26);
        for (auto word : words2) {
            vector<int> tmp(26);
            for (auto ch : word) {
                tmp[ch - 'a']++;
                v2[ch - 'a'] = max(v2[ch - 'a'], tmp[ch - 'a']);
            }
        }

        for (auto word : words1) {
            vector<int> v1(26);
            for (auto ch : word) {
                v1[ch - 'a']++;
            }
            bool valid = true;
            for (int i = 0; i < 26; i++) {
                if (v1[i] < v2[i]) {
                    valid = false;
                    break;
                }
            }

            if (valid)
                res.push_back(word);
        }

        return res;
    }
};