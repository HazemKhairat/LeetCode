class Solution:
    def totalFruit(self, f: List[int]) -> int:
        dic = Counter()
        i = 0
        res = 0

        for j in range(len(f)):
            dic[f[j]] += 1
            while len(dic) > 2:
                dic[f[i]] -= 1
                if dic[f[i]] == 0:
                    del dic[f[i]]
                i += 1
            
            res = max(res, j - i + 1)
        
        return res


