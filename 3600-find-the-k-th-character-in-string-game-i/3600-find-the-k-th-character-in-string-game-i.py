class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"

        while len(word) < k:
            for ch in word:
                tmp = ord(ch) + 1
                word += chr(tmp)
        
        return word[k - 1]