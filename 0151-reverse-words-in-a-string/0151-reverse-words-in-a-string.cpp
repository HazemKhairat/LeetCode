class Solution {
public:
    string reverseWords(string s) {
        vector<string> words;
        stringstream ss(s);
        string word;
        while (ss >> word) {
            words.push_back(word);
        }

        string res = "";
        for (int i = words.size() - 1; i > 0; i--) {
            res += words[i];
            res += ' ';
        }
        
        res += words[0];
        return res;
    }
};