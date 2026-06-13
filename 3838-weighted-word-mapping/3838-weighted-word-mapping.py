class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:

        def sumWord(word):
            res = 0
            for ch in word:
                idx = ord(ch) - 97
                res += weights[idx]
            return res
                

        arr = [chr(i) for i in range(122, 96, -1)]

        ans = ""
        for word in words:
            total = sumWord(word)
            total %= 26
            ans += arr[total]
            

        return ans
            
        