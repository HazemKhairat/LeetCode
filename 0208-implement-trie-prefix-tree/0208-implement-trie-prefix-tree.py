class TrieNode:
    def __init__(self):
        self.childs = {}
        self.wordEnd = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.childs:
                node.childs[ch] = TrieNode()

            node = node.childs[ch]

        node.wordEnd = True

    def search(self, word: str) -> bool:
        node = self.root

        for ch in word:
            if ch in node.childs:
                node = node.childs[ch]
            else:
                return False

        return node.wordEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch in node.childs:
                node = node.childs[ch]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
