class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        permutations = set()

        def solve(st):
            nonlocal k
            if len(st) >= n:
                k -= 1
                if k == 0:
                    return st
                return ""
            
            res = ""
            for i in range(1, n + 1):
                ch = str(i)
                if ch in st:
                    continue
                res = solve(st + ch)
                if res != "":
                    return res
            return res
        
        
        return solve("")