class Node {
public:
    Node* chars[26] = {};

    void put(char ch) { chars[ch - 'a'] = new Node(); }

    bool contain(char ch) { return chars[ch - 'a'] != NULL; }

    Node* next(char ch) { return chars[ch - 'a']; }
};

class Trie {
public:
    Node* root;
    Trie() { root = new Node(); }

    void insert(string& word) {
        Node* node = root;
        for (auto ch : word) {
            if (!node->contain(ch)) {
                node->put(ch);
            }
            node = node->next(ch);
        }
    }

    bool isPrefix(string& pref) {
        Node* node = root;
        for (auto ch : pref) {
            if (!node->contain(ch)) {
                return false;
            }
            node = node->next(ch);
        }
        return true;
    }
};

class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int count = 0;
        for (auto word : words) {
            Trie prefTrie;
            prefTrie.insert(word);
            if (prefTrie.isPrefix(pref)) {
                count++;
            }
        }

        return count;
    }
};