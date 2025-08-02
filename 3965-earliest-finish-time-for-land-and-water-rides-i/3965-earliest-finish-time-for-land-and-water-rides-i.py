class Solution:
    def earliestFinishTime(
        self, ls: List[int], ld: List[int], ws: List[int], wd: List[int]
    ) -> int:
        n = len(ls)
        m = len(ws)
        res = inf
        for i in range(n):
            for j in range(m):
                t = ls[i] + ld[i]
                if t >= ws[j]:
                    t += wd[j]
                else:
                    t = t + (ws[j] - t) + wd[j]
                res = min(res, t)

        for i in range(m):
            for j in range(n):
                t = ws[i] + wd[i]
                if t >= ls[j]:
                    t += ld[j]
                else:
                    t = t + (ls[j] - t) + ld[j]
                res = min(res, t)

        return res
