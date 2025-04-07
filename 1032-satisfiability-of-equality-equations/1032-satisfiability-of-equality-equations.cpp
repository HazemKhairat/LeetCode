class Solution {
public:
    unordered_map<char, char> parent;
    unordered_map<char, int> rank;
    bool equationsPossible(vector<string>& equations) {
        for (char ch = 'a'; ch <= 'z'; ch++) {
            parent[ch] = ch;
        }
        for (auto eq : equations) {
            if (eq[1] == eq[2]) {
                Union(eq[0], eq[3]);
            }
        }

        for (auto eq : equations) {
            char p1 = find(eq[0]), p2 = find(eq[3]);
            if (p1 == p2 && eq[1] == eq[2] || p1 != p2 && eq[1] != eq[2]) {
                continue;
            }
            return false;
        }

        return true;
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
        } else if (rank[p1] < rank[p2]) {
            parent[p1] = p2;
            rank[p1] += rank[p2];
        } else {
            parent[p2] = p1;
            rank[p2] += rank[p1];
        }
    }
};