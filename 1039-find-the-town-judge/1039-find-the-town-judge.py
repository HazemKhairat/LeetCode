class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: return 1
        cnt = [0] * (n + 1)
        l = 0
        ans = n
        for u, v in trust:
            cnt[v] += 1
        for i in range(1, n + 1):
            if cnt[i] == n - 1:
                l += 1
                ans = i
        if l > 1 or l == 0: return -1

        for u, v in trust:
            if ans == u:
                return -1
        
        return ans
        

