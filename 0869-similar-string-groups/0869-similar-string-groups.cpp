class Solution {
public:
    unordered_map<string, string> parent;
    unordered_map<string, int> rank;

    int numSimilarGroups(vector<string>& strs) {
        for (auto str : strs) {
            parent[str] = str;
        }
        /*
            int once = 1
            2 chs  * *
            tars
            rats
            if s[i] == s[j] or ( (s[i] = chs[0] or chs[1]) && (s[j] == chs[0] or
           chs[1])) continue else chs[0] = s[i], chs[1] = s[j] once--
            if(once == 0)
             union
        */

        for (int i = 0; i < strs.size(); i++) {
            string s1 = strs[i];
            for (int j = i + 1; j < strs.size(); j++) {
                int once = 1;
                vector<char> chs(2, '*');
                string s2 = strs[j];
                for (int k = 0; k < s1.size(); k++) {
                    if (s1[k] == s2[k] or
                        ((s1[k] == chs[0] or s1[k] == chs[1]) &&
                         (s2[k] == chs[0] or s2[k] == chs[1]))) {
                        continue;
                    } else {
                        chs[0] = s1[k], chs[1] = s2[k];
                        once--;
                    }
                }
                if (once >= 0) {
                    Union(s1, s2);
                }
            }
        }

        unordered_set<string> unique;
        for (auto str : strs) {
            string tmp = find(str);
            unique.insert(tmp);
        }

        return unique.size();
    }

    string find(string s) {
        if (parent[s] == s) {
            return s;
        }
        return parent[s] = find(parent[s]);
    }

    void Union(string s1, string s2) {
        string p1 = find(s1), p2 = find(s2);
        if (p1 == p2) {
            return;
        } else if (rank[p1] < rank[p2]) {
            parent[p1] = p2;
            rank[p1] += rank[p2];
        } else {
            parent[p2] = p1;
            rank[p2] += rank[p1];
        }
    }
};