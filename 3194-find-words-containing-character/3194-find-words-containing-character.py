class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []

        for index, word in enumerate(words):
            if x in word:
                res.append(index)
        
        return res