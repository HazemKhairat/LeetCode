class TrieNode:
    def __init__(self):
        self.childs = {}
        self.min_len = float("inf")
        self.idx = float("inf")


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

        for idx, s in enumerate(wordsContainer):
            trie.insert(s[::-1], idx)

        ans = []
        for s in wordsQuery:
            ans.append(trie.query(s[::-1]))

        return ans
