class TrieNode:
    def __init__(self):
        self.childs = {}
        self.min_len = inf
        self.idx = inf


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s, idx):

        node = self.root

        if len(s) < node.min_len:
            node.min_len = len(s)
            node.idx = idx

        for ch in s:
            if ch not in node.childs:
                node.childs[ch] = TrieNode()

            node = node.childs[ch]

            if len(s) < node.min_len:
                node.min_len = len(s)
                node.idx = idx

    def query(self, s):
        node = self.root

        for ch in s:
            if ch in node.childs:
                node = node.childs[ch]
            else:
                break

        return node.idx


class Solution:
    def stringIndices(
        self, wordsContainer: List[str], wordsQuery: List[str]
    ) -> List[int]:
        trie = Trie()
        ans = []

        for i, word in enumerate(wordsContainer):
            trie.insert(word[::-1], i)

        for q in wordsQuery:
            ans.append(trie.query(q[::-1]))

        return ans
