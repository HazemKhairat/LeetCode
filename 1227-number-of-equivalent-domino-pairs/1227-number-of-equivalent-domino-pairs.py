class Solution:
    def numEquivDominoPairs(self, dom: List[List[int]]) -> int:
        n = len(dom)

        cnt = Counter()
        res = 0
        for i in range(n):
            dom[i].sort()
            x = tuple(dom[i])
            cnt[x] += 1
            res += cnt[x] - 1

        return res
