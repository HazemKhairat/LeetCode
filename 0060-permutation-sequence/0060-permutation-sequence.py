class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ""

        def solve(st):
            nonlocal k, res

            if len(st) >= n:
                k -= 1
                if k == 0:
                    res = st
                return
            
            for i in range(1, n + 1):
                ch = str(i)
                if ch in st:
                    continue
                solve(st + ch)
                if res:
                    return        
        solve("")
        return res