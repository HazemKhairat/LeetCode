class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dic = set(wordDict)
        res = []

        def backtrack(idx, path):
            print(path)
            if idx == len(s):
                res.append(" ".join(path))
                return
            
            for i in range(idx, len(s) + 1):
                word = s[idx:i]
                if word in dic:
                    backtrack(i, path + [word])


        
        backtrack(0, [])
        return res