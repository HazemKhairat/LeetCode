class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        dic = defaultdict()
        for ch in s: dic[ch] = 0
        n = len(s)
        for i in range(n):
            dic[s[i]] += cost[i]

        ans = inf
        for i in range(26):
            ch = chr(97 + i)
            tmp = 0
            for key, val in dic.items():
                if key != ch:
                    tmp += val
            ans = min(ans, tmp)

        return ans if ans != inf else 0
                    