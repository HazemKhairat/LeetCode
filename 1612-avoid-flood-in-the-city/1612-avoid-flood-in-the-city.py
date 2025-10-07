class Solution:
    def avoidFlood(self, r: List[int]) -> List[int]:
        lastOcurr = Counter()
        s = SortedSet()
        n = len(r)
        ans = [1] * n

        for i in range(n):
            if r[i] == 0:
                s.add(i)
            else:
                ans[i] = -1
                if r[i] in lastOcurr:
                    idx = s.bisect(lastOcurr[r[i]])
                    if idx == len(s):
                        return []
                    ans[s[idx]] = r[i]
                    s.discard(s[idx])
                lastOcurr[r[i]] = i

        return ans
