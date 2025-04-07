
class Solution {
public:
    unordered_map<char, char> parent;

    string smallestEquivalentString(string s1, string s2, string baseStr) {
        // Initialize all 26 lowercase characters
        for (char ch = 'a'; ch <= 'z'; ch++) {
            parent[ch] = ch;
        }

        // Union the equivalences
        for (int i = 0; i < s1.size(); i++) {
            Union(s1[i], s2[i]);
        }

        // Build result from baseStr
        string res;
        for (int i = 0; i < baseStr.size(); i++) {
            char ch = find(baseStr[i]);
            res.push_back(ch);
        }
        return res;
    }

    char find(char ch) {
        if (parent[ch] == ch) {
            return ch;
        }
        return parent[ch] = find(parent[ch]);
    }

    void Union(char ch1, char ch2) {
        char p1 = find(ch1), p2 = find(ch2);
        if (p1 == p2) {
            return;
        }
        // Always keep the lexicographically smaller as parent
        else if (p1 < p2) {
            parent[p2] = p1;
        } else {
            parent[p1] = p2;
        }
    }
};