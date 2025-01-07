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
                if (isSubstringOf(text, words[j])) {
                    res.push_back(text);
                    break;
                }
            }
        }
        return res;
    }

    bool isSubstringOf(string subStr, string str) {
        for (int i = 0; i < str.size(); i++) {
            bool match = true;
            for (int j = 0; j < subStr.size(); j++) {
                if (i + j >= str.size() || str[i + j] != subStr[j]) {
                    match = false;
                    break;
                }
            }
            if (match)
                return match;
        }
        return false;
    }
};